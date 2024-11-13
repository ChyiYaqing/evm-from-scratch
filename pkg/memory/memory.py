class SimpleMemory:
    def __init__(self) -> None:
        self.memory = []
    
    def access(self, offset, size):
        return self.memory[offset:offset+size]
    
    def load(self, offset):
        return self.access(offset, 32)
    
    def store(self, offset, value):
        self.memory[offset:offset+len(value)] = value

class Memory(SimpleMemory):
    def store(self, offset, value):
        memory_expansion_cost = 0

        if len(self.memory) <= offset + len(value):
            expansion_size = 0

            # initialize memory with 32 zeros if it is empty
            if len(self.memory) == 0:
                expansion_size = 32
                self.memory = [0x00 for _ in range(32)]
            
            # extend memory more if needed
            if len(self.memory) < offset + len(value):
                expansion_size += offset + len(value) - len(self.memory)
                self.memory.extend([0x00] * expansion_size)
            
            memory_expansion_cost = expansion_size**2 # simplified
        
        super().store(offset, value)
        return memory_expansion_cost

def calc_memory_expansion_gas(memory_byte_size):
    memory_size_word = (memory_byte_size + 31) / 32
    memory_cost = (memory_size_word ** 2) / 512 + (3 * memory_size_word)
    return round(memory_cost)

if __name__ == '__main__':
    memory = Memory()
    memory.store(0, [0x01, 0x02, 0x03, 0x04])
    print(memory.load(0))