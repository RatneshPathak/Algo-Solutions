class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent, depth, size, heavy = [-1]*n, [0]*n, [1]*n, [-1]*n
        order = [0]
        for u in order:
            for v in g[u]:
                if v != parent[u]:
                    parent[v], depth[v] = u, depth[u] + 1
                    order.append(v)

        for u in order[::-1]:
            for v in g[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if heavy[u] == -1 or size[v] > size[heavy[u]]:
                        heavy[u] = v

        head, pos = [0]*n, [0]*n
        timer, stack = 0, [(0, 0)]
        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u], pos[u] = h, timer
                timer += 1
                for v in g[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))
                u = heavy[u]

        bit = [1 << (ord(c) - 97) for c in s]
        seg = [0] * (2 * n)
        for i in range(n):
            seg[n + pos[i]] = bit[i]
        for i in range(n - 1, 0, -1):
            seg[i] = seg[2*i] ^ seg[2*i+1]

        def update(p, x):
            p += n
            seg[p] = x
            while p > 1:
                p //= 2
                seg[p] = seg[2*p] ^ seg[2*p+1]

        def get(l, r):
            res = 0
            l, r = l + n, r + n + 1
            while l < r:
                if l & 1:
                    res ^= seg[l]
                    l += 1
                if r & 1:
                    r -= 1
                    res ^= seg[r]
                l //= 2
                r //= 2
            return res

        ans = []
        for q in queries:
            t, a, b = q.split()
            a = int(a)
            if t == "update":
                bit[a] = 1 << (ord(b) - 97)
                update(pos[a], bit[a])
            else:
                b = int(b)
                mask = 0
                while head[a] != head[b]:
                    if depth[head[a]] < depth[head[b]]:
                        a, b = b, a
                    mask ^= get(pos[head[a]], pos[a])
                    a = parent[head[a]]
                if depth[a] > depth[b]:
                    a, b = b, a
                mask ^= get(pos[a], pos[b])
                ans.append(mask & (mask - 1) == 0)
        return ans