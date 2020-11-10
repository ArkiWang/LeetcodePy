class Solution:
    def calculate(self, s: str) -> int:
        ops = []
        nums = []
        num = None
        for i in range(len(s)):
            print(ops)
            print(nums)
            if num != None and (s[i] < '0' or s[i] > '9'):
                nums.append(int(num))
                num = None
            if s[i] == '(':
                ops.append(s[i])
            elif s[i] == '+':
                if len(ops) == 0 or ops[len(ops)-1] == '(':
                    ops.append(s[i])
                else:
                    while len(ops) > 0 and ops[len(ops)-1] != '(':
                        op = ops.pop()
                        num2 = nums.pop()
                        num1 = nums.pop()
                        if op == '-':nums.append(num1-num2)
                        else:nums.append(num1+num2)
                    ops.append(s[i])

            elif s[i] == '-':
                if len(ops) == 0 or ops[len(ops)-1] == '(':
                    ops.append(s[i])
                else:
                    while len(ops) > 0 and ops[len(ops) - 1] != '(':
                        op = ops.pop()
                        num2 = nums.pop()
                        num1 = nums.pop()
                        if op == '+':nums.append(num1 + num2)
                        else:nums.append(num1 - num2)
                    ops.append(s[i])
            elif s[i] == ')':
                while len(ops) > 0:
                    op = ops.pop()
                    if op == '(':
                        break
                    num2 = nums.pop()
                    num1 = nums.pop()
                    if op == '+':
                        nums.append(num1+num2)
                    elif op == '-':
                        nums.append(num1-num2)
            elif s[i] >= '0' and s[i] <= '9':
                if num != None:
                    num = num*10 + int(s[i])
                else:
                    num = int(s[i])

        if num!= None: nums.append(num)

        while len(ops) > 0:
            num2 = nums.pop()
            num1 = nums.pop()
            op = ops.pop()
            if op == '+':
                nums.append(num1+num2)
            else:
                nums.append(num1-num2)
        return nums[0]

solution = Solution()
res = solution.calculate("(6)-(8)-(7)+(1+(6))")
print(res)








