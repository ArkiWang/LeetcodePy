# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    candidates = None
    flags = []

    def getAB(self, A: TreeNode, B: TreeNode):
        if A is not None:
            if A.val == B.val: self.candidates.append(A)
            self.getAB(A.left, B)
            self.getAB(A.right, B)

    def check(self, A: TreeNode, B: TreeNode):
        if A is not None and B is not None and A.val == B.val:
            self.flags.append(True)
            self.check(A.left, B.left)
            self.check(A.right, B.right)
        elif B is not None:
            self.flags.append(False)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None: return False
        self.candidates = []
        self.getAB(A, B)
        print(len(self.candidates))
        for a in self.candidates:
            print(a)
            self.flags = []
            self.check(a, B)
            if all(self.flags):
                return True
        return False

a = [3]
b = [1, 2, 3]
lb = ''
lb.join(b)
print(lb)