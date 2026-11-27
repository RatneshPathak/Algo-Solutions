class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        freq = [0] * 1501

        for f, p in items:
            freq[f] += 1

        dp = [0] * (budget + 1)

        for f, p in items:
            bonus = sum(freq[x] for x in range(f, 1501, f)) - 1
            old = dp[:]

            for b in range(p, budget + 1):
                dp[b] = max(dp[b], dp[b - p] + 1)
                dp[b] = max(dp[b], old[b - p] + bonus + 1)

        return max(dp)