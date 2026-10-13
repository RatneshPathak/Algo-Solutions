class Solution:
    def maxAlternatingSum(self, nums):
        nums.sort(key=lambda x: x * x, reverse=True)
        k = (len(nums) + 1) // 2
        squares = [x * x for x in nums]
        return sum(squares[:k]) - sum(squares[k:])