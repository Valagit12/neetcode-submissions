class TimeMap:

    def __init__(self):
        self.store = {} # string -> (stirng, int)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key] = self.store.get(key, [])
        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        returnable = ""
        lis = self.store.get(key, [])
        print(lis)
        low = 0
        high = len(lis) - 1

        while low <= high:

            mid = (low + high) // 2
        
            if lis[mid][1] == timestamp:
                return lis[mid][0]
            elif lis[mid][1] > timestamp:
                high = mid - 1
            else:
                returnable = lis[mid][0]
                low = mid + 1

        return returnable


        
