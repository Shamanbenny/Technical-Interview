def func_f(n : int):
    # Time Complexity: O(n(2n-1)) =~ O(n^2)
    print("func_f(" + str(n) + "): " + str(func_g(n, n)))
    print("Calculated answer: " + str((2*n-1) * n))

def func_g(n1: int, n2: int):
    sum = 0
    if (n1 < 1):
        return sum
    for _ in range(n2):
        sum += 1
    sum += func_g(n1/2, n2)
    sum += func_g(n1/2, n2)
    return sum

func_f(16)
func_f(32)