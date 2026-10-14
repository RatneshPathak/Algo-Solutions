class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        nines, remainder = divmod(sum, 9)
        ans = "9" * nines

        if remainder:
            ans += str(remainder)

        ans += "0" * (num - len(ans))
        return ans