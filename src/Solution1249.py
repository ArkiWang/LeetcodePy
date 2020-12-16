class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = []
        right = []
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == ')':
                if len(left) > 0:
                    left.pop()
                else:
                    right.append(i)
        res = ""
        s = list(s)
        for i, e in enumerate(s):
            if i not in left and i not in right:
                res = res + e
        return res

