class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}
        stack = [(0, False, None)]

        while stack:
            u, exiting, old = stack.pop()
            ch = s[u]

            if exiting:
                if old is None:
                    last.pop(ch)
                else:
                    last[ch] = old
                continue

            old = last.get(ch)
            if old is not None:
                new_parent[u] = old
            last[ch] = u

            stack.append((u, True, old))
            for v in reversed(children[u]):
                stack.append((v, False, None))

        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[new_parent[i]].append(i)

        ans = [1] * n
        order = [0]

        for u in order:
            order.extend(children[u])

        for u in reversed(order[1:]):
            ans[new_parent[u]] += ans[u]

        return ans