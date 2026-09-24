class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        right_arr = deque()
        res = deque()
        for a in asteroids:
            isLeft = a < 0
            if isLeft:
                print("insert", a, "to left")
                res.append(a)
                while right_arr:
                    b = right_arr.pop()
                    right_arr.append(b)
                    if abs(a) >= abs(b):
                        right_arr.pop()
                        print("pop", b, "from right")
                    if abs(a) <= abs(b):
                        res.pop()
                        print("pop", a, "from left")
                        break
            else:
                print("insert", a, "to right")
                right_arr.append(a)
        res += right_arr
        return list(res)
