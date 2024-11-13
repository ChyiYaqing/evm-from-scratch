def mload(evm): # Mload从偏移制定的内存中加载一个32字节，然后存放在栈中
    offset = evm.stack.pop()
    value = evm.memory.load(offset)
    evm.stack.push(value)
    evm.pc += 1

def mstore(evm): # 将一个32字节保存到内存中
    # TODO:  should be right aligend
    offset, value = evm.stack.pop(), evm.stack.pop()
    evm.memory.store(offset, value)
    evm.pc += 1

def mstore8(evm): # 将一个字节保存在内存中
    offset, value = evm.stack.pop(), evm.stack.pop
    evm.memory.store(offset, value)
    evm.pc += 1