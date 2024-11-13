from pkg.utils import utils

def byte(evm): # 从一个字中获取一个字节
    i, x = evm.stack.pop(), evm.stack.pop()
    if i >= 32:
        result = 0
    else:
        result = (x // pow(256, 31-i)) % 256
    evm.pc += 1
    evm.gas_dec(3)

def shl(evm): # 按位左移，1010按位左移2变成 101000
    shift, value = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(value << shift)
    evm.pc += 1
    evm.gas_dec(3)

def shr(evm): # 按位右移, 1010按位右移2变成10
    shift, value = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(value >> shift)
    evm.pc += 1
    evm.gas_dec(3)

def sar(evm): # 有符号右移
    shift, value = evm.stack.pop(), evm.stack.pop()
    if shift >= 256:
        result = 0 if value >= 0 else utils.UINT_255_NEGATIVE_ONE
    else:
        result = (value >> shift) & utils.UINT_256_MAX
    evm.stack.push(result)
    evm.pc += 1
    evm.gas_dec(3)