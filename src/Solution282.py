class Solution:
    resL = []
    def solver(self, rstr: str) -> int:
        '''
        spl = list(rstr)
        for i, e in enumerate:
            if e in ['+', '-', '*']:
                spl[i] = ' '
        spl = str(spl)
        spl.split(' ')

        :param rstr:
        :return:
        '''

        nums = []
        ops = []
        nL = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        i = 0
        while i < len(rstr):
            if rstr[i] in nL:
                tmp = ''
                while i < len(rstr) and rstr[i] in nL:
                    tmp += rstr[i]
                    i += 1
                i -= 1
                nums.append(int(tmp))
            else:
                if rstr[i] == '*':
                    ops.append(rstr[i])
                elif len(ops) == 0:
                    ops.append(rstr[i])
                else:
                    while len(ops) > 0:
                        op = ops.pop()
                        num2 = nums.pop()
                        num1 = nums.pop()
                        if op == '+':
                            nums.append(num1+num2)
                        elif op == '-':
                            nums.append(num1-num2)
                        else:
                            nums.append(num1*num2)
                    ops.append(rstr[i])
            i += 1
        while len(ops) > 0:
            op = ops.pop()
            num2 = nums.pop()
            num1 = nums.pop()
            if op == '+':
                nums.append(num1 + num2)
            elif op == '-':
                nums.append(num1 - num2)
            else:
                nums.append(num1 * num2)
        print(nums[0])
        return nums[0]

    # operator + - *
    def helper(self, num: [int], target: int, i: int, rstr: str):
        if i < len(num):
            self.helper(num, target, i+1, rstr + str(num[i]))
            self.helper(num, target, i+1, rstr + '+' + str(num[i]))
            self.helper(num, target, i+1, rstr + '-' + str(num[i]))
            self.helper(num, target, i+1, rstr + '*' + str(num[i]))
        elif self.solver(rstr) == target:
            self.resL.append(rstr)

    def addOperators(self, num: str, target: int) -> [str]:
        nnum = []
        for n in num:
            nnum.append(int(n))
        self.resL = []
        self.helper(nnum, target, 1, num[0])
        return self.resL

num = "123"
target = 6
num = "232"
target = 8
num = "105"
target = 5
sol = Solution()
res = sol.addOperators(num, target)
print(res)

