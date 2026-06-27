from collections import Counter

class Solution:
    def maximumLength(self, nums):
        freq = Counter(nums)
        ans = 1

        # Special case for 1
        if 1 in freq:
            if freq[1] % 2 == 0:
                ans = max(ans, freq[1] - 1)
            else:
                ans = max(ans, freq[1])

        for x in list(freq.keys()):
            if x == 1:
                continue

            cur = x
            length = 0

            while freq.get(cur, 0) >= 2:
                length += 2
                cur = cur * cur

            if freq.get(cur, 0) == 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans
