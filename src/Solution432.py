from cmath import inf
from collections import OrderedDict

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.vdic = OrderedDict()
        self.minv, self.mink = inf, ""
        self.maxv, self.maxk = 0, ""


    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.dic:
            self.dic[key] = 1
        else:
            self.dic[key] += 1

        if self.dic[key] not in self.vdic:
            self.vdic[self.dic[key]] = {key}
        else:
            self.vdic[self.dic[key]].add(key)

        if self.minv > self.dic[key]:
            self.minv = self.dic[key]
            self.mink = key
        if self.maxv < self.dic[key]:
            self.maxv = self.dic[key]
            self.maxk = key


    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.dic:
            if len(self.vdic[self.dic[key]]) > 1:
                self.vdic[self.dic[key]].remove(key)
            else:
                self.vdic.__delitem__(self.dic[key])

            if self.dic[key] == 1:
                self.dic.__delitem__(key)
            else:
                self.dic[key] -= 1

            if key == self.mink and self.minv not in self.vdic:
                for k in self.vdic.keys():
                    self.minv = k
                    self.mink = list(self.vdic[k])[0]
                    break
            if key == self.maxk and self.maxk not in self.vdic:
                for k in reversed(self.vdic.keys()):
                    self.maxv = k
                    self.maxk = list(self.vdic[k])[0]


    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return self.maxk


    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return self.mink