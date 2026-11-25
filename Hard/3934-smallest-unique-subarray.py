class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        rank = nums[:]
        sa = list(range(n))
        k = 1

        while k < n:
            sa.sort(key=lambda i: (
                rank[i],
                rank[i + k] if i + k < n else -1
            ))

            new_rank = [0] * n
            for j in range(1, n):
                a, b = sa[j - 1], sa[j]
                new_rank[b] = new_rank[a] + (
                    (rank[a], rank[a + k] if a + k < n else -1) !=
                    (rank[b], rank[b + k] if b + k < n else -1)
                )

            rank = new_rank
            k *= 2

        pos = [0] * n
        for i, s in enumerate(sa):
            pos[s] = i

        lcp = [0] * n
        h = 0

        for i in range(n):
            p = pos[i]
            if p == 0:
                h = 0
                continue

            j = sa[p - 1]
            while (i + h < n and j + h < n
                   and nums[i + h] == nums[j + h]):
                h += 1

            lcp[p] = h
            h = max(0, h - 1)

        ans = n

        for p in range(n):
            start = sa[p]
            common = max(
                lcp[p],
                lcp[p + 1] if p + 1 < n else 0
            )

            if common < n - start:
                ans = min(ans, common + 1)

        return ans