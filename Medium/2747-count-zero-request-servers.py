class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        from collections import defaultdict

        logs.sort(key=lambda a: a[1])
        ans = [0] * len(queries)
        cnt = defaultdict(int)
        l = r = 0

        for q, i in sorted((q, i) for i, q in enumerate(queries)):
            while r < len(logs) and logs[r][1] <= q:
                cnt[logs[r][0]] += 1
                r += 1
            while l < r and logs[l][1] < q - x:
                cnt[logs[l][0]] -= 1
                if not cnt[logs[l][0]]:
                    del cnt[logs[l][0]]
                l += 1
            ans[i] = n - len(cnt)

        return ans