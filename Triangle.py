class Solution:
    def minimumTotal(self, triangle):
        # Start from the last row
        dp = triangle[-1][:]

        # Traverse from second last row to top
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]
