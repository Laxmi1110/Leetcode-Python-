from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))
        
        vis = set([1])
        stack = [1]
        min_edge = float('inf')
        
        while stack:
            u = stack.pop()
            for v, d in graph[u]:
                min_edge = min(min_edge, d)
                if v not in vis:
                    vis.add(v)
                    stack.append(v)
        
        return min_edge
