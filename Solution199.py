# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def getRofEachLayer(self, roots: [], ans: []):
        if len(roots) > 0:
            ans.append(roots[-1].val)
            next = []
            for root in roots:
                if root.left is not None:
                    next.append(root.left)
                if root.right is not None:
                    next.append(root.right)
            self.getRofEachLayer(next, ans)

    def rightSideView(self, root: TreeNode) -> [int]:
        if root is None: return []
        ans = []
        self.getRofEachLayer([root], ans)
        return ans