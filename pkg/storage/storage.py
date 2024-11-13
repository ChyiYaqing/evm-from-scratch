class KeyValue:
    def __init__(self) -> None:
        self.storage = {}
    
    def load(self, key):
        return self.storage[key]
    
    def store(self, key, value):
        self.storage[key] = value

class Storage(KeyValue):
    def __init__(self) -> None:
        super().__init__()
        self.cache = []
    
    def load(self, key):
        warm = True if key in self.cache else False
        if not warm:
            self.cache.append(key)
        if key not in self.storage:
            return warm, 0x00
        return warm, super().load(key)

if __name__ == "__main__":
    storage = Storage()
    print(storage.load(1))
    storage.store(1, 420)
    print(storage.load(1))