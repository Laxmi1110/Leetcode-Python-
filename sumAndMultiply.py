from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        n = len(s)

        # Precompute powers of 10 modulo MOD
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # Build Segment Tree
        size = 1
        while size < n:
            size <<= 1

        # Each node stores: (non_zero_count, digit_sum, concatenated_value)
        seg = [(0, 0, 0)] * (2 * size)

        for i in range(n):
            if s[i] != '0':
                d = int(s[i])
                seg[size + i] = (1, d, d)

        for i in range(size - 1, 0, -1):
            left = seg[i * 2]
            right = seg[i * 2 + 1]
            cnt = left[0] + right[0]
            sm = left[1] + right[1]
            val = (left[2] * pow10[right[0]] + right[2]) % MOD
            seg[i] = (cnt, sm, val)

        def merge(a, b):
            return (
                a[0] + b[0],
                a[1] + b[1],
                (a[2] * pow10[b[0]] + b[2]) % MOD
            )

        def query(l, r):
            left_res = (0, 0, 0)
            right_res = (0, 0, 0)

            l += size
            r += size

            while l <= r:
                if l & 1:
                    left_res = merge(left_res, seg[l])
                    l += 1
                if not (r & 1):
                    right_res = merge(seg[r], right_res)
                    r -= 1
                l //= 2
                r //= 2

            return merge(left_res, right_res)

        ans = []
        for l, r in queries:
            _, digit_sum, value = query(l, r)
            ans.append((value * digit_sum) % MOD)

        return ans
