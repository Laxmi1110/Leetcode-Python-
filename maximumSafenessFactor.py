from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        # Step 1: Multi-source BFS to get dist to nearest thief
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    dist[r][c] = 0

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # Step 2: Binary search + BFS check
        def can_reach(min_safe):
            if dist[0][0] < min_safe:
                return False
            vis = [[False] * n for _ in range(n)]
            q = deque([(0, 0)])
            vis[0][0] = True

            while q:
                r, c = q.popleft()
                if r == n - 1 and c == n - 1:
                    return True
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not vis[nr][nc] and dist[nr][nc] >= min_safe:
                        vis[nr][nc] = True
                        q.append((nr, nc))
            return False

        lo, hi = 0, n + n # max Manhattan distance in n x n grid is 2n-2
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_reach(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return res
