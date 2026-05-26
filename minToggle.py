class Solution:
    def minToggle(self, arr):
        n = len(arr)

        # prefix1[i] = number of 1s from 0 to i-1
        prefix1 = [0] * (n + 1)

        for i in range(n):
            prefix1[i + 1] = prefix1[i] + (1 if arr[i] == 1 else 0)

        ans = n

        # Try every partition
        for i in range(n + 1):

            # 1s on left side need to become 0
            left_toggle = prefix1[i]

            # 0s on right side need to become 1
            right_zeros = (n - i) - (prefix1[n] - prefix1[i])

            ans = min(ans, left_toggle + right_zeros)

        return ans
