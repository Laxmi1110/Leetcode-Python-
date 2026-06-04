class Solution:
    def maxZeroOneDiff(self, s: str) -> int:
        max_sum = float('-inf')
        curr_sum = 0
        has_zero = False
        
        for ch in s:
            val = 1 if ch == '0' else -1
            if ch == '0':
                has_zero = True
                
            curr_sum = max(val, curr_sum + val)
            max_sum = max(max_sum, curr_sum)
        
        # If string has only 1s, per problem return -1
        if not has_zero:
            return -1
        
        return max_sum
