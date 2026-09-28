# LeetCode 1614 - Maximum Nesting Depth of the Parentheses
# Difficulty: Easy
#
# Problem:
# Given a valid parentheses string s, return the nesting depth of s.
# The nesting depth is the maximum number of nested parentheses.
#
# Example 1:
# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
#
# Example 2:
# Input: s = "(1)+((2))+(((3)))"
# Output: 3
#
# Example 3:
# Input: s = "()(())((()()))"
# Output: 3
#
# Constraints:
# 1 <= s.length <= 100
# s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
# It is guaranteed that s is a valid parentheses string.


class Solution:

    def maxDepth(self, s):
        depth = ans = 0

        for c in s:
            if c == "(":
                depth += 1
                ans = max(ans, depth)
            elif c == ")":
                depth -= 1

        return ans