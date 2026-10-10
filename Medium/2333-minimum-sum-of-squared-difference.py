class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        left, right = 0, max(diffs)

        while left < right:
            mid = (left + right) // 2
            needed = sum(max(0, d - mid) for d in diffs)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        ans = 0
        remaining = k

        for d in diffs:
            if d > level:
                remaining -= d - level
                ans += level * level
            else:
                ans += d * d

        if remaining > 0:
            ans -= remaining * (2 * level - 1)

        return ans