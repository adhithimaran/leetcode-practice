class LRUCache:
    LRU_map = {}
    last_updated = []

    def __init__(self, capacity: int):
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.LRU_map:
            self.last_updated.append(key)
            return self.LRU_map[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.LRU_map[key] = value
        if len(self.LRU_map) > self.capacity:
            least_used = self.last_updated[0]
            del self.LRU_map[least_used]
        self.last_updated.append(key)