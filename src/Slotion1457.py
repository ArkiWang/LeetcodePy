from copy import deepcopy
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    palindrome = 0
    def get_pre_path(self, root: TreeNode, path: str)->[]:
        if root != None:
            if root.left != None:self.get_pre_path(root.left, path + str(root.left.val))
            if root.right != None:self.get_pre_path(root.right, path + str(root.right.val))
            if root.left == None and root.right == None and self.check_pesudo_palindrome(path):
                self.palindrome += 1
                print(path)


    def check_pesudo_palindrome(self, path:str) -> bool:
        sdic = {}
        for i in range(len(path)):
            if path[i] not in sdic:
                sdic[path[i]] = 1
            else:
                num = sdic.get(path[i])
                sdic[path[i]] = num + 1
        print(sdic)
        not_has_odd = True
        for key in sdic:
            if sdic.get(key) % 2 != 0 and not_has_odd:
                not_has_odd = False
            elif sdic.get(key) % 2 != 0:
                return False
        return True

    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        if root == None: return 0;
        self.palindrome = 0
        self.get_pre_path(root, str(root.val))
        return self.palindrome

#["2","3","1","3","1","null","1"] str
def build_test_tree2(root: TreeNode, i: int, nodes: []) -> TreeNode:
    if i < len(nodes):
        if nodes[i] != "null":root.val = int(nodes[i])
        else:root.val = -1
        #if 2 * (i + 1) - 1 < len(nodes) and nodes[2 * (i + 1) - 1] != "null":
        root.left = TreeNode()
        build_test_tree(root.left, 2 * (i + 1) - 1, nodes)
        root.right = TreeNode()
        build_test_tree(root.right, 2 * (i + 1), nodes)

def build_test_tree(root: TreeNode, i: int, nodes: []) -> TreeNode:
    if i < len(nodes):
        if nodes[i] != "null":root = TreeNode(nodes[i])
        else:root = TreeNode(-1)
        #if 2 * (i + 1) - 1 < len(nodes) and nodes[2 * (i + 1) - 1] != "null":
        build_test_tree(root.left, 2 * (i + 1) - 1, nodes)
        build_test_tree(root.right, 2 * (i + 1), nodes)

def hierarchy_order(root):
    now_nodes = [root]
    next_nodes = []
    while len(now_nodes) > 0:
        while len(now_nodes) > 0:
            p = now_nodes.pop()
            print(p.val)
            if p.left!=None:next_nodes.insert(0, p.left)
            if p.right!=None:next_nodes.insert(0, p.right)
        now_nodes = deepcopy(next_nodes)
        next_nodes.clear()

strs = ["2","3","1","3","1","null","1"]
root = TreeNode()
build_test_tree(root, 0, strs)
hierarchy_order(root)
