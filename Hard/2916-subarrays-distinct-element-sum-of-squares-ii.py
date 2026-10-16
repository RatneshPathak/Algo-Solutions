class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n

        tree = [0] * size
        lazy = [0] * size
        last = {}
        ans = 0

        def push(node, start, end):
            if lazy[node] == 0 or start == end:
                return

            val = lazy[node]
            mid = (start + end) // 2

            for child, length in (
                (node * 2, mid - start + 1),
                (node * 2 + 1, end - mid)
            ):
                tree[child] = (
                    tree[child] + 2 * val * tree_sum[child]
                    + val * val * length
                ) % MOD
                tree_sum[child] = (
                    tree_sum[child] + val * length
                ) % MOD
                lazy[child] += val

            lazy[node] = 0

        tree_sum = [0] * size

        def update(node, start, end, left, right):
            if left <= start and end <= right:
                length = end - start + 1
                tree[node] = (
                    tree[node] + 2 * tree_sum[node] + length
                ) % MOD
                tree_sum[node] = (tree_sum[node] + length) % MOD
                lazy[node] += 1
                return

            push(node, start, end)
            mid = (start + end) // 2

            if left <= mid:
                update(node * 2, start, mid, left, right)
            if right > mid:
                update(node * 2 + 1, mid + 1, end, left, right)

            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD
            tree_sum[node] = (
                tree_sum[node * 2] + tree_sum[node * 2 + 1]
            ) % MOD

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1
            update(1, 0, n - 1, left, i)
            last[x] = i
            ans = (ans + tree[1]) % MOD

        return ans