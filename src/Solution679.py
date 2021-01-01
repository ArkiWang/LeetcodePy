import copy
from cmath import inf, log
import numpy as np

class Solution:
    suffix_list = None
    tree_list = None
    shuffle_list = None
    op_list = None
    num_list = None
    flag = False
    post_tree = None
    post_trees = None

    gen_combine_peer_layer = None
    def which_to_gen(self, parent:[], i, res):
        if i < len(parent):
            self.which_to_gen(parent, i+1, res)
            res.append(parent[i])
            self.which_to_gen(parent, i+1, res)
            res.pop()
        elif len(res) > 0 and res not in self.gen_combine_peer_layer:
            self.gen_combine_peer_layer.append(copy.deepcopy(res))


    def generator(self, n, cnt, layer, tree):
        if cnt < n and pow(2, layer) < len(tree):
            parent = []
            for k in range(pow(2, layer), pow(2, layer+1)):
                if 2*k+1 < len(tree) and tree[k] == 1:
                    parent.append(k)
            self.gen_combine_peer_layer = []
            self.which_to_gen(parent, 0, [])
            for gen in self.gen_combine_peer_layer:
                for p in gen:
                    tree[p], tree[2*p], tree[2*p+1] = 2, 1, 1
                self.generator(n, cnt+2*len(gen), layer+1, tree)
                for p in gen:
                    tree[p], tree[2*p], tree[2*p+1] = 1, 0, 0
        elif cnt == n and tree not in self.tree_list:
            self.tree_list.append(copy.deepcopy(tree))


    def generate_suffix(self, nums: [], ops: [],  ptree:[]):
        i, j = 0, 0
        res = []
        for k in range(len(ptree)):
            if ptree[k] == 1:
                res.append(nums[i])
                i += 1
            else:
                res.append(ops[j])
                j += 1
        return res


    def select_combine(self, ops: []):
        for i, ei in enumerate(ops):
            for j, ej in enumerate(ops):
                for k, ek in enumerate(ops):
                    if [ei, ej, ek] not in self.op_list:
                        self.op_list.append([ei, ej, ek])

    def shuffle(self, nums: [], i=0) -> []:
        if i < len(nums):
            for k in range(len(nums)):
                self.shuffle(nums, i + 1)
                nums[i], nums[k] = nums[k], nums[i]
                self.shuffle(nums, i + 1)
        elif nums not in self.shuffle_list:
            self.shuffle_list.append(copy.deepcopy(nums))

    def calcu(self, suffix:[]):
        nums = []
        for i,e in enumerate(suffix):
            if e in ['+', '-', '*', '/']:
                num2 = nums.pop()
                num1 = nums.pop()
                if e == '+':
                    nums.append(num1+num2)
                elif e == '-':
                    nums.append(num1-num2)
                elif e == '*':
                    nums.append(num1*num2)
                else:
                    nums.append(num1/max(num2,0.000000000000001))
            else:
                nums.append(e)
        return nums[0]


    def get_post_tree(self, i, tree:[]):
        if i < len(tree) and tree[i] != 0:
            self.get_post_tree(2*i, tree)
            self.get_post_tree(2*i+1, tree)
            self.post_tree.append(tree[i])



    def judgePoint24(self, nums: [int]) -> bool:
        self.shuffle_list = []
        self.op_list = []
        self.shuffle(nums)
        self.num_list = copy.deepcopy(self.shuffle_list)
        self.select_combine(['+', '-', '*', '/'])
        self.shuffle_list = []
        while len(self.op_list) > 0:
            ol = self.op_list.pop()
            self.shuffle(ol)
        self.op_list = self.shuffle_list

        n = 7
        length = int((n+1)/2)
        length = int(pow(2, length)) + 1
        tree = [0] * length
        tree[1] = 1
        self.tree_list = []
        #self.generate_tree(7, 1, 1, tree)
        self.generator(7,1,0,tree)
        #print(self.tree_list)
        self.post_trees = []
        for tree in self.tree_list:
            self.post_tree = []
            self.get_post_tree(1, tree)
            self.post_trees.append(copy.deepcopy(self.post_tree))
        #print(self.post_trees)

        self.suffix_list = []
        for tree in self.post_trees:
            for nl in self.num_list:
                for ol in self.op_list:
                    self.suffix_list.append(self.generate_suffix(nl, ol, tree))
        #print(self.suffix_list)

        for suffix in self.suffix_list:
            res = self.calcu(suffix)
            if abs(res-24) <= 0.0000000000001:
                return True

        return False

['#', 2, 1, '+', 9, 1, '-', '*', '#', '#', '#', '#', '#', '#', '#', '#', '#']
nums = [1,9,1,2]

nums = [1,3,4,6]
nums = [4, 1, 8, 7]
nums = [3,3,8,8]

sol = Solution()
res = sol.judgePoint24(nums)
print(res)