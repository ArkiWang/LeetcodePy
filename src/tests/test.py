from functools import partial

import numpy as np
class A:
    Acnt = 0
    def __init__(self):
        self.cnt=0

    def modifyAcnt(self, add: int):
        A.Acnt += add

    def modifycnt(self, add: int):
        self.cnt += add

a1 = A()
a1.modifyAcnt(3)
a1.modifycnt(233)
print(a1.Acnt, a1.cnt)
a2 = A()
print(a2.Acnt)
l = [0,1,2,3,4,5,6,7]
print(np.all([i == 0 for i in l]))
print(l[0:-2])
dl = []
dl = dict(zip(l,[0]*7))
print(dl)

def helloworld(s: str) -> None:
    print("helloworld", s)

hw = helloworld
hw("arki")

arr = [[1,3,4],[2,3,6]]
a = np.asarray(arr)
cnt = (a == 3).sum(axis=-1)
print("cnt=",cnt)
print(a[cnt])
for (xi, i) in enumerate(arr):
    print("xi: ",xi," i: ",i)
evals = list(map(int, [1.2e5, 6e5, 3e6]))
print("evals: ",evals)
maxevals = 3e6

ru = np.random.uniform(-0.1,0.1,100)
print("ru: ",ru)

a = np.asarray(np.random.uniform(1,15,20))
print("a: ", a)
print("clip a:",np.clip(a,2,12))
lower = 3; upper = 9
check = partial(np.clip, a_min=lower, a_max=upper)
print("partial a:",check(a))