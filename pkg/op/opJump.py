from opCode import *

def jump(evm):
    counter = evm.stack.pop()

    # make sure that we jump to an JUMPDEST opcode
    if not evm.program[counter] == JUMPDEST:
        raise Exception("Can only jump to JUMPDEST")
    
    evm.pc = counter
    evm.gas_dec(8)

def jumpi(evm):
    counter, b = evm.stack.pop(), evm.stack.pop()

    if b != 0:
        evm.pc = counter
    else:
        evm.pc += 1
    evm.gas_dec(10)

def pc(evm):
    evm.stack.push(evm.pc)
    evm.pc += 1
    evm.gas_dec(2)

def jumpdest(evm):
    evm.pc += 1
    evm.gas_dec(1)