# Definition for a binary tree node.
from cmath import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    ans = -inf
    def isValidBST(self, root, minVal=-inf, maxVal=inf):
            if root == None:
                return True
            if root.val >= maxVal or root.val <= minVal:
                return False
            return self.isValidBST(root.left, minVal, root.val) and self.isValidBST(root.right, root.val, maxVal)
    def getSum(self, node):
            if node is not None:
                lsum = self.getSum(node.left)
                rsum = self.getSum(node.right)
                nsum = node.val + lsum + rsum
                self.ans = max(self.ans, nsum)
                return nsum
            else:
                return 0
    def maxSumBST(self, root: TreeNode) -> int:
        self.ans = -inf
        def calcu(root):
            if root is not None:
                if(self.isValidBST(root)):
                    self.getSum(root)
                    return
                calcu(root.left)
                calcu(root.right)
        calcu(root)
        return max(0, self.ans)

root = TreeNode(4)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
sol = Solution()
ans = sol.maxSumBST(root)
print(ans)