class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        print('get', key)
        ans = self.cache.get(key)
        if ans:
            self.cache.pop(key)
            self.cache[key] = ans
            return ans 
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        'LRU ->          <-MRU'
        print('put', key, value)
        if self.cache.get(key):
            self.cache.pop(key)
            self.cache[key] = value
            return
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
        
