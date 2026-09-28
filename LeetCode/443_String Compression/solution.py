class Solution:
    def compress(self, chars: list[str]) -> int:
        n = 0
        i = 0

        while i < len(chars):
            curr = chars[i]
            count = 0
            while i < len(chars) and chars[i] == curr:
                count += 1
                i += 1
            chars[n] = curr
            n += 1
            if count > 1:
                for char in str(count):
                    chars[n] = char
                    n += 1
        """
        Here, chars would be spliced if the input array must reflect the true answer.
        But the question doesn't really care for that so we'll skip the following:
        """
        # print(chars)
        # chars = chars[:n]
        # print(chars)
        return n

