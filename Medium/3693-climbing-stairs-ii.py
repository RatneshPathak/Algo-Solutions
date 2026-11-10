from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] + [float('inf')] * n
        for j in range(1, n + 1):
            dp[j] = costs[j - 1] + min(
                dp[i] + (j - i) ** 2
                for i in range(max(0, j - 3), j)
            )
        return dp[n]