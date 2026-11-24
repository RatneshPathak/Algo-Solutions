class Solution:
    def maxLength(self, nums: List[int]) -> int:
        from math import gcd

        ans = 0
        n = len(nums)

        for i in range(n):
            prod = 1
            g = 0
            l = 1

            for j in range(i, n):
                x = nums[j]
                prod *= x
                g = gcd(g, x)
                l = l * x // gcd(l, x)

                if prod == l * g:
                    ans = max(ans, j - i + 1)

        return ans