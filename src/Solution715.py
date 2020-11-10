class RangeModule:

    def __init__(self):
        self.lefts = []
        self.rights = []

    def crossedRange(self, left: int, right: int) -> []:
        pos = []
        for i in range(len(self.lefts)):
            if not (left >= self.rights[i] or right <= self.lefts[i]):
                pos.append(i)
        return pos

    def unionRanges(self, left: int, right: int, cps: []) -> None:
        ls = [self.lefts[i] for i in cps] + [left]
        rs = [self.rights[i] for i in cps] + [right]
        min_left = left
        max_right = right
        for i in range(len(ls)):
            min_left = min(ls[i], min_left)
            max_right = max(rs[i], max_right)
        i = 0
        for p in cps:
            self.lefts.pop(p + i)
            self.rights.pop(p + i)
            i -= 1
        self.lefts.append(min_left)
        self.rights.append(max_right)

    def addRange(self, left: int, right: int) -> None:
        cps = self.crossedRange(left, right)
        for i in range(len(self.lefts)):
            if self.lefts[i] == right and i not in cps:
                cps.append(i)
            if self.rights[i] == left and i not in cps:
                cps.append(i)
        cps.sort()
        if len(cps) == 0:
            self.lefts.append(left)
            self.rights.append(right)
        else:
            self.unionRanges(left, right, cps)
        print(self.lefts)
        print(self.rights)

    def queryRange(self, left: int, right: int) -> bool:
        for i in range(len(self.lefts)):
            if left >= self.lefts[i] and right <= self.rights[i]:
                return True
        return False

    def delfromithRange(self, left: int, right: int, i: int) -> int:
        if left <= self.lefts[i] and right >= self.rights[i]:
            self.lefts.pop(i)
            self.rights.pop(i)
            return 1
        if left >= self.lefts[i] and right <= self.rights[i]:
            if left == self.lefts[i]:
                self.lefts[i] = right
            elif right == self.rights[i]:
                self.rights[i] = left
            else:
                r = self.rights[i]
                self.rights[i] = left
                self.lefts.append(right)
                self.rights.append(r)
        elif self.rights[i] >= left and self.rights[i] <= right:
            self.rights[i] = left
        elif self.lefts[i] >= left and self.lefts[i] <= right:
            self.lefts[i] = right
        print(self.lefts)
        print(self.rights)
        return 0

    def removeRange(self, left: int, right: int) -> None:
        cps = self.crossedRange(left, right)
        if len(cps) != 0:
            mins = 0
            for p in cps:
                mins += self.delfromithRange(left, right, p - mins)

# Your RangeModule object will be instantiated and called as such:
orders = ["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"]
keys = [[],[10,20],[14,16],[10,14],[13,15],[16,17]]
orders = ["RangeModule","addRange","addRange","addRange","queryRange","queryRange","queryRange","removeRange","queryRange"]
keys = [[],[10,180],[150,200],[250,500],[50,100],[180,300],[600,1000],[50,150],[50,100]]
orders = ["RangeModule","addRange","removeRange","removeRange","addRange","removeRange","addRange","queryRange","queryRange","queryRange"]
keys = [[],[6,8],[7,8],[8,9],[8,9],[1,3],[1,8],[2,4],[2,9],[4,6]]
orders = ["RangeModule","addRange","queryRange","removeRange","removeRange","addRange","queryRange","addRange","queryRange","removeRange"]
keys = [[],[5,8],[3,4],[5,6],[3,6],[1,3],[2,3],[4,8],[2,3],[4,9]]
orders = ["RangeModule","addRange","addRange","removeRange","queryRange","removeRange","addRange","queryRange","addRange","addRange","queryRange","removeRange","addRange","removeRange","queryRange","removeRange","removeRange","removeRange","addRange","queryRange","queryRange","queryRange","addRange","queryRange","addRange","queryRange","removeRange","removeRange","addRange","removeRange","queryRange","addRange","removeRange","removeRange","removeRange","removeRange","queryRange","addRange","removeRange","queryRange","queryRange","removeRange","queryRange","addRange","removeRange","removeRange","queryRange","addRange","removeRange","addRange","addRange","removeRange","queryRange","removeRange","addRange","removeRange","addRange","removeRange","removeRange","addRange","queryRange","queryRange","queryRange","queryRange","queryRange","removeRange","addRange","queryRange","addRange","addRange","queryRange","removeRange","queryRange","queryRange","addRange","addRange","queryRange","addRange","queryRange","removeRange","addRange","addRange","removeRange","queryRange","removeRange","queryRange","addRange","addRange","queryRange","removeRange","addRange"]
keys = [[],[9,80],[30,86],[1,32],[48,91],[19,39],[8,91],[24,25],[24,90],[15,80],[36,64],[25,81],[32,46],[5,37],[34,79],[30,40],[34,74],[1,20],[49,69],[30,72],[56,80],[21,50],[23,68],[33,43],[43,97],[40,96],[47,93],[19,67],[39,69],[9,61],[36,77],[51,100],[25,37],[41,81],[73,100],[24,75],[23,56],[21,90],[4,93],[15,72],[8,27],[2,85],[43,84],[9,55],[26,63],[11,100],[75,77],[42,69],[50,93],[45,59],[76,99],[11,57],[25,71],[20,56],[74,95],[77,78],[52,88],[38,61],[39,90],[27,28],[46,67],[5,45],[53,99],[52,64],[1,37],[60,83],[8,85],[37,92],[10,67],[9,20],[99,100],[80,82],[40,57],[44,78],[10,16],[45,90],[63,85],[16,65],[50,82],[31,87],[50,54],[13,68],[40,85],[46,92],[24,35],[27,54],[25,93],[9,36],[12,24],[64,97],[20,27]]
for i,e in enumerate(orders):
    if e == "RangeModule":
        obj = RangeModule()
    elif e == "addRange":
        obj.addRange(keys[i][0], keys[i][1])
    elif e == "removeRange":
        obj.removeRange(keys[i][0], keys[i][1])
    elif e == "queryRange":
        param_2 = obj.queryRange(keys[i][0], keys[i][1])
        print(param_2)
