def _pop(evm): # 从栈中探出一个
    evm.pc += 1
    evm.gas_dec(2)
    evm.stack.pop(0)