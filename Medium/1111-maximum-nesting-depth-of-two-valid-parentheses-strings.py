class Solution:
    def maxDepthAfterSplit(self, seq):
        ans = []
        depth = 0

        for c in seq:
            if c == '(':
                depth += 1
                ans.append(depth % 2)
            else:
                ans.append(depth % 2)
                depth -= 1

        return ans