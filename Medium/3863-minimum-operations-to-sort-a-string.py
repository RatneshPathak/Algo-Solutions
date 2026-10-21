class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        sorted_s = "".join(sorted(s))

        if s == sorted_s:
            return 0

        if n == 2:
            return -1

        mn = sorted_s[0]
        mx = sorted_s[-1]

        if s[0] == mn or s[-1] == mx:
            return 1

        if mn in s[1:-1] or mx in s[1:-1]:
            return 2

        return 3
