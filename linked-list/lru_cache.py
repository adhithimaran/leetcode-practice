class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU_map = {}
        self.last_updated = []

    def get(self, key: int) -> int:
        if key in self.LRU_map:
            self.update(key)
            return self.LRU_map[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRU_map:
            self.LRU_map[key] = value
            self.update(key)
            return
        if len(self.LRU_map) >= self.capacity:
            least_used = self.last_updated.pop(0)
            del self.LRU_map[least_used]
        self.LRU_map[key] = value
        self.update(key)
    
    def update(self, key: int) -> None:
        if key in self.last_updated:
            self.last_updated.remove(key)
        self.last_updated.append(key)
