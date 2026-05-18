class Solution:
    def maxSum(self, n):
        memo = {}

        def solve(x):
            # Base case
            if x == 0:
                return 0

            # If already calculated
            if x in memo:
                return memo[x]

            # Maximum of current number or recursive break
            memo[x] = max(
                x,
                solve(x // 2) + solve(x // 3) + solve(x // 4)
            )

            return memo[x]

        return solve(n)
