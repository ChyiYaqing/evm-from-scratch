from pkg.utils import utils

def lt(evm): # less than
    a, b = evm.stack().pop(), evm.stack.pop()
    evm.stack.push(1 if a < b else 0)
    evm.pc += 1
    evm.gas_dec(3)

def slt(evm): # signed less than
    a, b = evm.stack.pop(), evm.stack.pop()
    a = utils.unsigned_to_signed(a)
    b = utils.unsigned_to_signed(b)
    evm.stack.push(1 if a < b else 0)
    evm.pc += 1
    evm.gas_dec(3)

def gt(evm): # greater than
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(1 if a > b else 0)
    evm.pc += 1
    evm.gas_dec(3)

def sgt(evm): # signed greater than
    a, b = evm.stack.pop(), evm.stack.pop()
    a = utils.unsigned_to_signed(a)
    b = utils.unsigned_to_signed(b)
    evm.stack.push(1 if a > b else 0)
    evm.pc += 1
    evm.gas_dec(3)

def eq(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(1 if a == b else 0)
    evm.pc += 1
    evm.gas_dec(3)

def iszero(evm):
    a = evm.stack.pop()
    evm.stack.push(1 if a == 0 else 0)
    evm.pc += 1
    evm.gas_dec(3)