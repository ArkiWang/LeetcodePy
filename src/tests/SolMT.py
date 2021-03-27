from statistics import mode

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    smin, nsmin = 0, 0
    def rob(self, root: TreeNode):
        def dfs(node: TreeNode):
            if node is None:
                return [0, 0]
            l = dfs(node.left)
            r = dfs(node.right)
            selected = node.val + l[1] + r[1]
            self.smin = min(self.smin, node.val)
            notSelected = max(l[0], l[1]) + max(r[0], r[1])
            if l[0] >= l[1]:
                self.nsmin = min(self.nsmin, node.left.val)
            if r[0] >= r[1]:
                self.nsmin = min(self.nsmin, node.right.val)
            return [selected, notSelected]
        self.smin, self.nsmin = 0, 0
        rootStatus = dfs(root)
        if rootStatus[0] > rootStatus[1]:
            return rootStatus[0], self.smin
        elif rootStatus[0] == rootStatus[1]:
            return rootStatus[0], min(self.smin, self.nsmin)
        else:
            return rootStatus[1], self.nsmin

    def getmode(self, a:[int]) -> int:
        dic = {}
        for k in a:
            if k not in dic:
                dic[k] = 1
            else:
                dic[k] += 1
        dic = dict(sorted(dic.items(), key=lambda kv:kv[1]))
        dic = dict(sorted(dic.items(), key=lambda kv:kv[0]))
        print(dic)
        return list(dic.keys())[0]

a = [3,3,2,2,5,5]
sol = Solution()
res = sol.getmode(a)
print(res)
