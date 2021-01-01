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
                    tree[2*p], tree[2*p+1] = 1, 1
                self.generator(n, cnt+2*len(gen), layer+1, tree)
                for p in gen:
                    tree[2*p], tree[2*p+1] = 0, 0
        elif cnt == n and tree not in self.tree_list:
            self.tree_list.append(copy.deepcopy(tree))


    def generate_suffix(self, nums: [], ops: [],  tree:[], i, j, k, suffix):
        if k < len(tree) and (len(nums) > 0 or len(ops) > 0):
            if tree[k] == 1:
                if 2*k+1 < len(tree) and tree[2*k] == 1 and tree[2*k+1] == 1 and len(ops) > 0:
                    suffix[k] = ops.pop()
                    self.generate_suffix(nums, ops, tree, i, j, 2*k, suffix)
                    self.generate_suffix(nums, ops, tree, i, j, 2*k+1, suffix)
                elif len(nums) > 0:
                    suffix[k] = nums.pop()
                    self.generate_suffix(nums, ops, tree, i, j, 2*k, suffix)
                    self.generate_suffix(nums, ops, tree, i, j, 2*k+1, suffix)
        elif  len(nums) == 0 and len(ops) == 0 and suffix not in self.suffix_list:
            self.suffix_list.append(copy.deepcopy(suffix))

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

    def calcu(self, suffix:[], i):
        if not self.flag and i < len(suffix):
            if suffix[i] != '#':
                if suffix[i] in ['+', '-', '*', '/']:
                    self.calcu(suffix, 2*i)
                    self.calcu(suffix, 2*i+1)
                    if 2*i+1 < len(suffix) and suffix[2*i] not in ['+', '-', '*', '/', '#'] and suffix[2*i+1] not in ['+', '-', '*', '/', '#']:
                        if suffix[i] == '+':
                            suffix[i] = suffix[2*i] + suffix[2*i+1]
                        elif suffix[i] == '-':
                            suffix[i] = suffix[2 * i] - suffix[2 * i + 1]
                        elif suffix[i] == '*':
                            suffix[i] = suffix[2 * i] * suffix[2 * i + 1]
                        else:
                            if suffix[2 * i + 1] != 0:
                                suffix[i] = suffix[2 * i] / suffix[2 * i + 1]
                            else:
                                suffix[i] = inf
                        suffix[2 * i], suffix[2 * i + 1] = '#', '#'
                    if i == 1:
                        print(suffix[1])
                        if suffix[1] == 24:
                            self.flag = True





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
        self.suffix_list = []
        for tree in self.tree_list:
            for nl in self.num_list:
                for ol in self.op_list:
                    suffix = ['#'] * length
                    dnl = copy.deepcopy(nl)
                    dol = copy.deepcopy(ol)
                    self.generate_suffix(dnl, dol, tree, 0, 0, 1, suffix)


        self.flag = False
        for suffix in self.suffix_list:
            self.calcu(suffix, 1)

        return self.flag

['#', 2, 1, '+', 9, 1, '-', '*', '#', '#', '#', '#', '#', '#', '#', '#', '#']
nums = [1,9,1,2]

nums = [1,3,4,6]
nums = [4, 1, 8, 7]
nums = [3,3,8,8]
sol = Solution()
res = sol.judgePoint24(nums)
print(res)