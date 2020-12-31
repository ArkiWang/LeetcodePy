import copy
from cmath import inf


class Solution:
    shuffle_list = None
    num_list = None
    op_list = None
    flag = False
    def shuffle(self, nums: [], i=0) ->[]:
        if i < len(nums):
            for k in range(len(nums)):
                self.shuffle(nums, i+1)
                nums[i], nums[k] = nums[k], nums[i]
                self.shuffle(nums, i+1)
        elif nums not in self.shuffle_list:
            self.shuffle_list.append(copy.deepcopy(nums))

    def calcu(self):
        for nums in self.num_list:
            for ops in self.op_list:
                ntmp = copy.deepcopy(nums)
                otmp = copy.deepcopy(ops)
                while len(otmp) > 0:
                    num2 = ntmp.pop()
                    num1 = ntmp.pop()
                    op = otmp.pop()
                    if op == '+':
                        ntmp.append(num1 + num2)
                    elif op == '-':
                        ntmp.append(num1 - num2)
                    elif op == '*':
                        ntmp.append(num1 * num2)
                    else:
                        if num2 != 0:
                            ntmp.append(num1 / num2)
                        else:
                            ntmp.append(inf)
                print(ntmp[0])
                if ntmp[0] == 24:
                    return True
        return False




    def select_combine(self, ops: [], m=3):
        for k in range(len(ops)):
            if k + 1 < len(ops):
                tmp = ops[:k] + ops[k+1:]
            else:
                tmp = ops[:k]
            self.op_list.append(tmp)


    def judgePoint24(self, nums: [int]) -> bool:
        self.flag = False
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

        print(len(self.num_list))
        print(self.num_list)
        print(len(self.op_list))
        print(self.op_list)
        return self.calcu()


nums = [6, 6, 6, 6]
nums = [4, 1, 8, 7]
nums = [1, 3, 4, 6]
sol = Solution()
res = sol.judgePoint24(nums)
print(res)