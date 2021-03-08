import numpy as np
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def helper(self, root: TreeNode, dic: {}):
        if root != None:
            dic[str(root)] = [str(root.left), str(root.right)]
            self.helper(root.left, dic)
            self.helper(root.right, dic)

    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        dic1, dic2 = {}, {}
        self.helper(t1, dic1)
        self.helper(t2, dic2)
        for key2 in dic2.keys():
            if key2 in dic1 and dic1[key2] == dic2[key2]:
                continue
            else:
                return False
        return True

