class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        value = -1
        if key in self.cache:
            value = self.cache.get(key)
            self.cache.__delitem__(key)
            self.cache[key] = value
        return value

    def getlength(self) -> int:
        return len(self.cache)

    def removefirst(self):
        if self.getlength() == 0:return
        keys = list(self.cache.keys())
        self.cache.__delitem__(keys[0])

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and self.getlength() < self.capacity:
            self.cache[key] = value
        elif key in self.cache:
            self.cache.__delitem__(key)
            self.cache[key] = value
        elif self.getlength() == self.capacity and key not in self.cache:
            self.removefirst()
            self.cache[key] = value



orders = ["LRUCache","put","put","get","put","get","put","get","get","get"]
kvs = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
orders = ["LRUCache","get","put","get","put","put","get","get"]
kvs = [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
#orders = ["LRUCache","put","put","put","put","get","get"]
#kvs = [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
for i in range(len(orders)):
    if orders[i] == "LRUCache":
        obj = LRUCache(kvs[i][0])
    elif orders[i] == "get":
        param = obj.get(kvs[i][0])
    elif orders[i] == "put":
        obj.put(kvs[i][0], kvs[i][1])
    print(obj.cache)

