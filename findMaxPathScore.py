from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List, k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        max_cost = 0
        for u, v, c in edges:
            adj[u].append((v, c))
            max_cost = max(max_cost, c)

        def can_reach(min_edge: int) -> bool:
            dp = [float('inf')] * n
            dp[0] = 0

            # Process nodes in topological order
            # Since it's a DAG, we can do n-1 relaxations
            for _ in range(n - 1):
                updated = False
                for u in range(n):
                    if dp[u] == float('inf'):
                        continue
                    for v, c in adj[u]:
                        if not online[v] or c < min_edge:
                            continue
                        if dp[u] + c < dp[v]:
                            dp[v] = dp[u] + c
                            updated = True
                if not updated:
                    break

            return dp[n-1] <= k

        left, right = 0, max_cost
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if can_reach(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
