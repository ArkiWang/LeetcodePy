#monotonous increase stack
class MonotonStack(object):
    def __init__(self):
        self.stack = [int]
        self.pointer = -1

    def push(self, e: int) -> []:
        pop = []
        while self.stack[self.pointer] < e:
            pop.append(self.stack.pop(self.pointer))
            self.pointer -= 1
        self.stack.append(e)
        self.pointer += 1
        return pop

    def pop(self) -> int:
        if self.pointer < 0 or self.pointer >= self.length():
            return None
        res = self.stack.pop(self.pointer)
        self.pointer -= 1
        return res

    def getpointer(self) -> int:
        return self.pointer

    def length(self) -> int:
        return self.pointer + 1

    def isempty(self) -> bool:
        if self.pointer == -1:
            return True
        else:
            return False
