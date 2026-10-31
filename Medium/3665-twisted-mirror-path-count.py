class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        get = (lambda r, c: grid[r][c]) if len(grid) >= len(grid[0]) else (lambda r, c: grid[c][r])
        dp = [[0, 0] for _ in range(min(len(grid), len(grid[0])) + 1)]
        dp[1] = [1, 1]

        for r in range(max(len(grid), len(grid[0]))):
            for c in range(len(dp) - 1):
                if get(r, c):
                    dp[c + 1] = [dp[c + 1][1], dp[c][0]]
                else:
                    dp[c + 1] = [(dp[c + 1][1] + dp[c][0]) % MOD] * 2

        return dp[-1][0]