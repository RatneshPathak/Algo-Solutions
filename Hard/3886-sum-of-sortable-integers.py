class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        sorted_nums = sorted(nums)
        ans = 0

        def is_rotation(a, b):
            k = len(a)
            doubled = a + a[:-1]

            lps = [0] * k
            j = 0
            for i in range(1, k):
                while j and b[i] != b[j]:
                    j = lps[j - 1]
                if b[i] == b[j]:
                    j += 1
                    lps[i] = j

            j = 0
            for x in doubled:
                while j and x != b[j]:
                    j = lps[j - 1]
                if x == b[j]:
                    j += 1
                    if j == k:
                        return True
            return False

        for k in range(1, n + 1):
            if n % k:
                continue

            if all(
                is_rotation(nums[i:i + k], sorted_nums[i:i + k])
                for i in range(0, n, k)
            ):
                ans += k

        return ans