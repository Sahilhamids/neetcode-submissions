class TimeMap:

    def __init__(self):
        self.hashtable = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashtable[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashtable:
            return ""
        ls = self.hashtable[key]
        left ,right= 0 , len(ls)-1
        res = ""
        while left <= right:

            mid = left + (right-left)//2

            if ls[mid][0] <= timestamp:
                res = ls[mid][1]
                left = mid +1
            else:
                right = mid -1
        return res
        
