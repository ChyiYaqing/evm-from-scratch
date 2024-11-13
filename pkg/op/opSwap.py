"""
将栈顶部的值域给定位置的栈中值交换
"""
def _swap(evm, n):
    value1, value2 = evm.stack.get(0), evm.stack.get(n+1)
    evm.stack.set(0, value2)
    evm.stack.set(n+1, value1)

    evm.pc += 1
    evm.gas_dec(3)