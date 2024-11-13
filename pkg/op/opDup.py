"""
通过将栈中值复制一份放入栈顶
"""
def _dup(evm, n):
    # make sure stack is big enough!
    value = evm.stack[n]
    evm.stack.push(value)

    evm.pc += 1
    evm.gas_dec(3)