def sload(evm): # 
    key = evm.stack.pop()
    warm, value = evm.storage.load(key)
    evm.stack.push(value)

    if warm:
        evm.gas_dec(100)
    else:
        evm.gas_dec(2100)
    evm.pc += 1

def sstore(evm):
    key, value = evm.stack.pop(), evm.stack.pop()
    warm, old_value = evm.storage.store(key, value)

    base_dynamic_gas = 0

    if value != old_value:
        if old_value == 0:
            base_dynamic_gas = 20000
        else:
            base_dynamic_gas = 2900
    
    access_cost = 100 if warm else 2100
    evm.gas_dec(base_dynamic_gas + access_cost)

    evm.pc += 1
    # TODO: do refunds