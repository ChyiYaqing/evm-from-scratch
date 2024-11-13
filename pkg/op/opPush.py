def _push(evm, n):
    evm.pc += 1
    evm.gas_dec(3)

    value = []
    for _ in range(n):
        value.append(evm.peek())
        evm.pc += 1
    evm.stack.push(int(''.join(map(str, value))))