class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree()->TreeNode:
    return TreeNode(3)

root = buildTree()
print(root.val)

l = [0,1,2,3,4,5]
print(l[1:3])

tl = [[1,2,3],[4,5,6],[7,8],[9]]
if tl.__contains__(5):
    print("5 is in the 2d-list")
else:
    print("can't figure out the inner level of the multi-dimensional vector")


def replaceSpace(s: str) -> str:
    return s.replace(" ", "%20")
    res = ""
    for i in range(len(s)):
        if s[i] == " ":
            pass
        else:
            res += s[i]
    return str

res = replaceSpace("fuck you lettcode")
print(res)

dtest = {0: 1, 1: 2, 2: 3}
print(dtest[0])
dtest.__delitem__(0)
print(dtest)
dtest[0] = 1
print(dtest)

l = "abbbadc"
l = sorted(l)
print(l)