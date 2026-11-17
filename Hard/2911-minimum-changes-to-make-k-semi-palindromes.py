class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[n] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                for d in range(1, length):
                    if length % d:
                        continue

                    changes = 0
                    for r in range(d):
                        left = i + r
                        right = j - d + 1 + r

                        while left < right:
                            changes += s[left] != s[right]
                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for end in range(2, n + 1):
            for parts in range(1, min(k, end // 2) + 1):
                for start in range((parts - 1) * 2, end - 1):
                    dp[end][parts] = min(
                        dp[end][parts],
                        dp[start][parts - 1] + cost[start][end - 1]
                    )

        return dp[n][k]