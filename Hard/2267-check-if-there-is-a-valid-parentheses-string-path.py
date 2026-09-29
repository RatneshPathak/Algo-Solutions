class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j].add(1)
                    continue

                prev = set()

                if i > 0:
                    prev |= dp[i - 1][j]

                if j > 0:
                    prev |= dp[i][j - 1]

                for balance in prev:
                    new_balance = balance + (1 if grid[i][j] == '(' else -1)

                    if 0 <= new_balance <= m + n:
                        dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]