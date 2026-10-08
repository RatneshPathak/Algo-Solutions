class Solution:
    def removeOuterParentheses(self, s):
        ans = []
        depth = 0

        for c in s:
            if c == '(':
                if depth > 0:
                    ans.append(c)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    ans.append(c)

        return ''.join(ans)