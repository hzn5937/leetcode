class TimeMap:

    def __init__(self):
        # { key : [value, timestamp] }
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_store:
            return ""
        values = self.key_store[key]
        target = timestamp

        left, right = 0, len(values) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= target:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)