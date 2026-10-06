class Solution:
    def minAddToMakeValid(self, s):
        balance = 0
        ans = 0

        for c in s:
            if c == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    ans += 1

        return ans + balance