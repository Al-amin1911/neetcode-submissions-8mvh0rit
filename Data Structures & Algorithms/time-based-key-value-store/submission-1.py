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
        for val, time in list_s:
            if time <= timestamp:
                fallback = val
            else:
                break
        return fallback

        