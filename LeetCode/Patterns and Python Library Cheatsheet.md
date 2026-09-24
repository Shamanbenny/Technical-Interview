# LeetCode Patterns and Python Library Cheatsheet

A small reference for recurring tools and patterns used in this repository.

## Python library essentials

### `deque`: fast queues and double-ended queues

```python
from collections import deque

q = deque(["a", "b"])
q.append("c")       # add on the right
q.appendleft("z")   # add on the left
first = q.popleft()  # remove from the left: O(1)
last = q.pop()       # remove from the right: O(1)
q.rotate(-1)         # move the left side to the right
q.reverse()          # reverse the deque in place
```

Use `deque` instead of `list.pop(0)`: removing from the front of a list is `O(n)`, while `append`, `appendleft`, `pop`, and `popleft` are approximately `O(1)` operations for a deque. `reverse()` changes the deque in place.

### `Counter`: frequency tables

```python
from collections import Counter

counts = Counter(["a", "b", "a"])
counts["a"]             # 2
counts["missing"]       # 0, rather than KeyError
counts.most_common(1)   # [("a", 2)]
counts.update("abc")
```

Common uses: character frequencies, duplicate detection, anagram checks, and tracking the number of available items.

### `bisect`: insertion points in sorted data

```python
import bisect

nums = [1, 2, 2, 4]
left = bisect.bisect_left(nums, 2)   # 1: first index with value >= 2
right = bisect.bisect_right(nums, 2) # 3: first index with value > 2
```

The value does not need to exist in the list. `bisect` returns the index where the value could be inserted while keeping the list sorted:

```python
nums = [1, 2, 4, 7]
bisect.bisect_left(nums, 3)   # 2: insert between 2 and 4
bisect.bisect_right(nums, 3)  # 2: same boundary because 3 is absent
```

This is especially useful when the index itself is the answer: finding the first value at least a threshold, splitting values into `< target` and `>= target`, or locating where a prefix-sum calculation should divide the array.

The names describe the two boundaries:

- `bisect_left(a, x)` returns the first valid insertion point before existing `x` values.
- `bisect_right(a, x)` returns the first valid insertion point after existing `x` values.

Both searches are `O(log n)`. The list must already be sorted.

## Pattern: cyclic or round-robin queue simulation

For [#649 Dota2 Senate](649_Dota2%20Senate/README.md), the official problem describes a round-based procedure and tags it with `Queue`. A useful name for the implementation is **cyclic queue simulation** or **round-robin queue simulation**. The Python documentation also uses `round-robin` for repeatedly cycling through active iterators.

The key trick is to store each item's index. When an item survives one pass, append its index plus `n`, which represents its position in the next cycle without physically rotating the original string.

```python
from collections import deque

def predictPartyVictory(senate: str) -> str:
    n = len(senate)
    radiant = deque()
    dire = deque()

    for i, party in enumerate(senate):
        (radiant if party == "R" else dire).append(i)

    while radiant and dire:
        r = radiant.popleft()
        d = dire.popleft()

        if r < d:
            radiant.append(r + n)  # R acts first and survives to next round
        else:
            dire.append(d + n)

    return "Radiant" if radiant else "Dire"
```

Pattern recognition: use this when entities are processed in order, removed when defeated, and surviving entities return after the current pass.

## Pattern: prefix sums for constant-time range sums

Build one extra prefix element so that `prefix[i]` means “the sum of the first `i` values.”

```python
prefix = [0]
for value in nums:
    prefix.append(prefix[-1] + value)

# Sum of nums[left:right], where right is exclusive:
range_sum = prefix[right] - prefix[left]
```

This turns each range-sum query into `O(1)` after `O(n)` preprocessing.

## Pattern: sorting + prefix sum + binary search

See [#2602 Minimum Operations to Make All Array Elements Equal](2602_Minimum%20Operations%20to%20Make%20All%20Array%20Elements%20Equal/README.md).

When many queries ask for the total distance from every value to a `target`, sort the values first:

```python
from bisect import bisect_left

nums.sort()
prefix = [0]
for value in nums:
    prefix.append(prefix[-1] + value)

target = ...  # current query
left_idx = bisect_left(nums, target) # first index with nums[i] >= target
n = len(nums)

left_cost = target * left_idx - prefix[left_idx]
right_sum = prefix[n] - prefix[left_idx]
right_cost = right_sum - target * (n - left_idx)
total_cost = left_cost + right_cost
```

### Why this works: discrete area under the adjustment graph

Imagine the sorted values as histogram bars and draw a horizontal line at `target`.

![Prefix-sum adjustment areas](2602_Solution%20Visual%20for%20Minimum%20Operations%20to%20Make%20All%20Array%20Elements%20Equal.png)

For every value before `left_idx`, the value is below `target`. The purple bars represent `sum(nums[:left_idx])`. The blue area left after subtracting those purple bars is the total left adjustment:

```text
target * left_idx - sum(nums[:left_idx])
```

For every value from `left_idx` onward, the value is at least `target`. The red region represents `target * (n - left_idx)`. The prefix sum of the entire suffix, `prefix[n] - prefix[left_idx]`, covers both the red region and the orange region. Subtracting the red region leaves the total right adjustment highlighted in orange:

```text
sum(nums[left_idx:]) - target * (n - left_idx)
```

The prefix array supplies both sums immediately, while `bisect_left` locates the boundary. This is a **sorting + prefix sum + binary search** pattern; “area under the histogram” is the visual model for why the arithmetic works. The red region is the target baseline used in the subtraction; it does not mean that the sorted values after `left_idx` are below `target`.

Typical complexity:

- Sort once: `O(n log n)`
- Build prefix sums: `O(n)`
- Answer each query: `O(log n)`

## Sources

- [Python `collections` documentation](https://docs.python.org/3/library/collections.html)
- [Python `bisect` documentation](https://docs.python.org/3/library/bisect.html)
- [LeetCode 649: Dota2 Senate](https://leetcode.com/problems/dota2-senate/)
- [LeetCode 2602: Minimum Operations to Make All Array Elements Equal](https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/)
