class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if val > root.val:
            tmp = TreeNode(val)
            tmp.left = root
            root = tmp
            return root
        def helper(p, root, val):
            if root is not None:
                #print(root.val)
                if  root.right is None and val < root.val:
                    root.right = TreeNode(val)
                elif root.val < val:
                    tmp = TreeNode(val)
                    tmp.left = p.right
                    p.right = tmp
                else:
                    helper(root, root.right, val)
        helper(None, root, val)
        return root