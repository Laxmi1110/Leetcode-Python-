class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1

        # Build adjacency list
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # BFS to find max depth from node 1
        from collections import deque
        q = deque([1])
        vis = [False] * (n + 1)
        vis[1] = True
        depth = -1

        while q:
            depth += 1
            for _ in range(len(q)):
                u = q.popleft()
                for v in g[u]:
                    if not vis[v]:
                        vis[v] = True
                        q.append(v)

        # depth = number of edges from root to deepest node
        if depth == 0:
            return 0
        return pow(2, depth - 1, MOD)
