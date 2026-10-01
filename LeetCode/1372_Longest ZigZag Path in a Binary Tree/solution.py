# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        def dfs(curr):
            if not curr:
                return [-1, -1, -1] # (leftPath, rightPath)
            maxLeft = dfs(curr.left)
            maxRight = dfs(curr.right)
            newMax = max(maxLeft[1] + 1, maxRight[0] + 1, maxLeft[2], maxRight[2])
            return [maxLeft[1] + 1, maxRight[0] + 1, newMax]

        ans = dfs(root)
        return ans[2]
