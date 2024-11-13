def revert(evm):
    offset, size = evm.stack.pop(), evm.stack.pop()
    evm.returndata = evm.memory.access(offset, size)

    evm.stop_flag = True
    evm.revert_flag = True
    evm.pc += 1
    evm.gas_dec(0)