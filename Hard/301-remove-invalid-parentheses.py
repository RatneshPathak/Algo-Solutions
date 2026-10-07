class Solution:
    def removeInvalidParentheses(self, s):
        left = right = 0

        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left:
                    left -= 1
                else:
                    right += 1

        ans = set()

        def dfs(i, left, right, balance, path):
            if i == len(s):
                if left == 0 and right == 0 and balance == 0:
                    ans.add(''.join(path))
                return

            c = s[i]

            if c == '(':
                if left > 0:
                    dfs(i + 1, left - 1, right, balance, path)

                path.append(c)
                dfs(i + 1, left, right, balance + 1, path)
                path.pop()

            elif c == ')':
                if right > 0:
                    dfs(i + 1, left, right - 1, balance, path)

                if balance > 0:
                    path.append(c)
                    dfs(i + 1, left, right, balance - 1, path)
                    path.pop()

            else:
                path.append(c)
                dfs(i + 1, left, right, balance, path)
                path.pop()

        dfs(0, left, right, 0, [])
        return list(ans)