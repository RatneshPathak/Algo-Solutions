class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        from bisect import bisect_left

        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)
        a = [bisect_left(vals, v) + 1 for v in nums]
        cnt, sm = [0] * (m + 1), [0] * (m + 1)

        def update(i, c, s):
            while i <= m:
                cnt[i] += c
                sm[i] += s
                i += i & -i

        def query(bit, i):
            res = 0
            while i:
                res += bit[i]
                i -= i & -i
            return res

        def kth(k):
            i, bit = 0, 1 << (m.bit_length() - 1)
            while bit:
                j = i + bit
                if j <= m and cnt[j] < k:
                    i = j
                    k -= cnt[j]
                bit >>= 1
            return i + 1

        costs = []
        total = 0

        for i, v in enumerate(nums):
            update(a[i], 1, v)
            total += v

            if i >= x:
                update(a[i-x], -1, -nums[i-x])
                total -= nums[i-x]

            if i >= x - 1:
                p = kth((x + 1) // 2)
                med = vals[p-1]
                c = query(cnt, p)
                s = query(sm, p)
                costs.append(med*c - s + total - s - med*(x-c))

        inf = float('inf')
        prev = [0] * (n + 1)

        for _ in range(k):
            curr = [inf] * (n + 1)
            for i in range(x, n + 1):
                curr[i] = min(curr[i-1], prev[i-x] + costs[i-x])
            prev = curr

        return prev[n]