from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                prev = set()
                if i:
                    prev |= dp[i - 1][j]
                if j:
                    prev |= dp[i][j - 1]
                dp[i][j] = {x ^ grid[i][j] for x in prev}

        return min(dp[-1][-1])