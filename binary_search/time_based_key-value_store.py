from collections import defaultdict
class TimeMap:
    # Time: O(log(n))
    # Space: O(1)
    def __init__(self):
        self.store = defaultdict(list) # key = string, value = [list of (value, timestamp)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ''
        values = self.store.get(key, [])

        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] < timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
