class Solution:
    def singleNumber(self, nums):
        ans = 0

        for i in range(32):
            count = 0

            for num in nums:
                if (num >> i) & 1:
                    count += 1

            if count % 3:
                ans |= (1 << i)

        # Handle negative numbers
        if ans >= 2**31:
            ans -= 2**32

        return ans
