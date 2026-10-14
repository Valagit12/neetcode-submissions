class TimeMap:

    def __init__(self):
        self.store = {} # string -> (stirng, int)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key] = self.store.get(key, [])
        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        returnable = ""
        print(self.store)
        for k in self.store.get(key, []):
            if k[1] <= timestamp:
                returnable = k[0]
        
        return returnable


        
