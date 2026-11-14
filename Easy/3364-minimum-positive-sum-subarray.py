class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')
        n = len(nums)

        for i in range(n):
            total = 0
            for j in range(i, min(n, i + r)):
                total += nums[j]
                if l <= j - i + 1 and total > 0:
                    ans = min(ans, total)

        return ans if ans != float('inf') else -1