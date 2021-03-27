class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.lcnt = 0
        self.rcnt = 0

class Solution:
    res = 0
    def getInsert(self, x: int, root: Node):
        if x <= root.val:
            root.lcnt += 1
            self.res += root.rcnt + (1 if root.val > x else 0)
            if root.left is None:
                return root
            else:
                return self.getInsert(x, root.left)

        else:
            root.rcnt += 1
            if root.right is None:
                return root
            else:
                return self.getInsert(x, root.right)



    def insertTree(self, x: int, root: Node):
        if root is None:
            root = Node(x)
            return root
        p = self.getInsert(x, root)
        if x <= p.val:
            p.left = Node(x)
        else:
            p.right = Node(x)
        return root

    def reversePairs(self, nums: [int]) -> int:
        self.res = 0
        root = None
        for x in nums:
            root = self.insertTree(x, root)
            print(self.res)
        return self.res

nums = [7,5,6,4]
nums = [1,3,2,3,1]
nums = [1,1,-1,-1,-1,1]
sol = Solution()
res = sol.reversePairs(nums)
print(res)