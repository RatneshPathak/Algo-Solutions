class Solution:
    def minSwaps(self, nums):
        def digit_sum(x):
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {num: i for i, num in enumerate(sorted_nums)}
        visited = [False] * len(nums)
        ans = 0

        for i in range(len(nums)):
            if visited[i] or pos[nums[i]] == i:
                continue

            cycle = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle += 1

            ans += cycle - 1

        return ans