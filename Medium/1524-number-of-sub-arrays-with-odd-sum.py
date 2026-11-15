class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even, odd = 1, 0
        ans = prefix = 0

        for x in arr:
            prefix += x
            if prefix % 2:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1

        return ans % MOD