from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges):
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            nodes = 1
            edge_count = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    a, b = dfs(nei)
                    nodes += a
                    edge_count += b

            return nodes, edge_count

        for i in range(n):
            if not visited[i]:
                nodes, edge_count = dfs(i)

                actual_edges = edge_count // 2
                required_edges = nodes * (nodes - 1) // 2

                if actual_edges == required_edges:
                    ans += 1

        return ans
