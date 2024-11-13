"""
临时存储:
    这些操作码的行为几乎和存储相同，但每次交易后都会丢弃变更
"""
def tload(evm):
    key = evm.stack.pop()
    warm, value = evm.storage.load(key)
    evm.stack.push(value)

    evm.gas_dec(100)
    evm.pc += 1

def tstore(evm):
    key, value = evm.stack.pop(), evm.stack.pop()
    evm.storage.store(key, value)
    evm.gas_dec(100)
    evm.pc += 1