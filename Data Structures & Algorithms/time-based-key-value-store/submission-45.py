class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))
        
        

    def get(self, key: str, timestamp: int) -> str:

        print(timestamp)
        liststr = self.storage[key]

        if not liststr:
            return ''
        liststr.sort()

        res = ''
        
        l = 0
        r = len(liststr) - 1
        mid = (l + r + 1) // 2
        while l <= r:
            print(l, mid, r)
            mid = (l + r) // 2
            midvalue, lvalue, rvalue = liststr[mid][0], liststr[l][0], liststr[r][0]

        
            # if timestamp > lvalue and timestamp < midvalue and mid - l <= 1:
            #     return liststr[l][1]

            if midvalue == timestamp:
                return liststr[mid][1]
            
            elif midvalue < timestamp:
                res = liststr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
            

        return res


    '''

    1 indexed
    {
        Alice: [(1, happy), (3, sad)]
    }


    1 - {Alice: Happy}
    2 - 
    3 - {Alice: Sad}
    4 - {}
    '''
        
