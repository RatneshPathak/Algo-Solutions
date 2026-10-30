class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        from heapq import heappush, heappop

        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        h = [(0, 0, 1)]

        while h:
            d, u, c = heappop(h)
            if d != dist[u][c]:
                continue
            if u == n - 1:
                return d

            for v, w in g[u]:
                nc = c + 1 if labels[u] == labels[v] else 1
                if nc <= k and d + w < dist[v][nc]:
                    dist[v][nc] = d + w
                    heappush(h, (d + w, v, nc))

        return -1