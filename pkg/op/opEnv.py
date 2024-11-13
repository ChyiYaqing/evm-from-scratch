def address(evm): # 返回当前执行此程序的账户地址
    evm.stack.push(evm.sender)
    evm.pc += 1
    evm.gas_dec(3)

def balance(evm): # 获取指定地址的余额
    address = evm.stack.pop()
    evm.stack.push(999999999)

    evm.pc += 1
    evm.gas_dec(2600) # 100 if warm

def origin(evm): #最初触发执行的地址
    evm.stack.push(evm.sender)
    evm.pc += 1
    evm.gas_dec(2)

def caller(evm): 
    evm.stack.push("0x414b60745072088d013721b4a28a0559b1A9d213")
    evm.pc += 1
    evm.gas_dec(2)

def callvalue(evm):
    evm.stack.push(evm.value)
    evm.pc += 1
    evm.gas_dec(2)

def calldataload(evm):
    i = evm.stack.pop()
    delta = 0
    if i+32 > len(evm.calldata):
        delta = i+32 - len(evm.calldata)
    
    # always has to be 32 bytes
    # if its not we append 0x00 bytes until it is
    calldata = evm.calldata[i:i+32-delta]
    calldata += 0x00*delta

    evm.stack.push(calldata)
    evm.pc += 1
    evm.gas_dec(3)

def calldatasize(evm): # 将调用数据的大小压入栈中
    evm.stack.push(len(evm.calldata))
    evm.pc += 1
    evm.gas_dec(2)

def calldatacopy(evm): # 将调用数据存储在内存
    destOffset = evm.stack.pop()
    offset = evm.stack.pop()
    size = evm.stack.pop()

    calldata = evm.calldata[offset:offset+size]
    memory_expansion_cost = evm.memory.store(destOffset, calldata)

    static_gas = 3
    minimum_word_size = (size + 31) // 32
    dynamic_gas = 3 * minimum_word_size + memory_expansion_cost

    evm.gas_dec(static_gas + dynamic_gas)
    evm.pc += 1

def codesize(evm): # 将当前正在运行的程序大小放入栈中
    evm.stack.push(len(evm.program))
    evm.pc += 1
    evm.gas_dec(2)

def codecopy(evm): # 将程序指定部分存储在内存中
    destOffset = evm.stack.pop()
    offset = evm.stack.pop()
    size = evm.stack.pop()

    code = evm.program[offset: offset+size]
    memory_expansion_cost = evm.memory.store(destOffset, code)

    static_gas = 3
    minimum_word_size = (size + 31) / 32
    dynamic_gas = 3 * minimum_word_size + memory_expansion_cost

    evm.gas_dec(static_gas + dynamic_gas)
    evm.pc += 1

def gasprice(evm): # 当前的Gas价格
    evm.stack.push(0x00) # 由于我们在本地运行所有操作，因此gas价格为0
    evm.pc += 1
    evm.gas_dec(2)

def extcodesize(evm): # 另一个程序的大小
    address = evm.stack.pop()
    evm.stack.push(0x00) # 在我们简化中没有其他程序
    evm.gas_dec(2600) # 100 if warm
    evm.pc += 1

def extcodecopy(evm): # 将另一个程序的执行部分存储在内存中
    address = evm.stack.pop()
    destOffset = evm.stack.pop()
    offset = evm.stack.pop()
    size = evm.stack.pop()

    extcode = [] # no external code
    memory_expansion_cost = evm.memory.store(destOffset, extcode)

    # refactor this in seperate method
    minimum_word_size = (size + 31) / 32
    dynamic_gas = 3 * minimum_word_size + memory_expansion_cost
    address_access_cost = 2600 # 100 if warm else 2600

    evm.gas_dec(dynamic_gas + address_access_cost)
    evm.pc += 1

def returndatasize(evm): # 从当前环境中获取上一次调用的输出数据大小
    evm.stack.push(0x00) # no return data
    evm.pc += 1
    evm.gas_dec(2)

def returndatacopy(evm): # 将先前返回数据的制定部分存储在内存中
    destOffset = evm.stack.pop()
    offset = evm.stack.pop()
    size = evm.stack.pop()

    returndata = evm.program[offset:offset+size]
    memory_expansion_cost = evm.memory.store(destOffset, returndata)

    minimum_word_size = (size + 31)/32
    dynamic_gas = 3 * minimum_word_size + memory_expansion_cost

    evm.gas_dec(3 + dynamic_gas)
    evm.pc += 1

def extcodehash(evm): # 外部程序的哈希值由其地址给出
    address = evm.stack.pop()
    evm.stack.push(0x00) # no code

    evm.gas_dec(2600) # 100 if warm
    evm.pc += 1

def blockhash(evm): # 获取最近256个完整块之一的哈希值，并将其推送到栈上
    blockNumber = evm.stack.pop()
    if blockNumber > 256:
        raise Exception("Only last 256 blocks can accessed")
    evm.stack.push(0x1cbcfa1ffb1ca1ca8397d4f490194db5fc0543089b9dee43f76cf3f962a185e8)
    evm.pc += 1
    evm.gas_dec(20)

def coinbase(evm): # 获取此区块的矿工地址
    evm.stack.push(0x1cbcfa1ffb1ca1ca8397d4f490194db5fc0543089b9dee43f76cf3f962a185e8)
    evm.pc += 1
    evm.gas_dec(2)