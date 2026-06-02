class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hash_map[key]:
            self.hash_map[key].append((value, timestamp))
        else:
            self.hash_map[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.hash_map[key]:
            return ""
        list_s = self.hash_map[key]
        fallback = ""
        l, r = 0, len(list_s)-1
        while l <= r:
            mid = (l+r)//2
            if list_s[mid][1] <= timestamp:
                fallback = list_s[mid][0]
                l = mid+1
            else:
                r = mid-1
        return fallback

        