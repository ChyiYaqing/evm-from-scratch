def add(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(a+b)
    evm.pc += 1
    evm.gas_dec(3)

def sub(evm):
    a,b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(a-b)
    evm.pc += 1
    evm.gas_dec(3)

def mul(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(a*b)
    evm.pc += 1
    evm.gas_dec(5)

def div(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(0 if b == 0 else a // b)
    evm.pc += 1
    evm.gas_dec(5)

pos_or_neg = lambda number: -1 if number < 0 else 1

def sdiv(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    sign = pos_or_neg(a*b)
    evm.stack.push(0 if b==0 else sign * (abs(a) // abs(b)))
    evm.pc += 1
    evm.gas_dec(5)

def mod(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(0 if b == 0 else a % b)
    evm.pc += 1
    evm.gas_dec(5)

def smod(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    sign = pos_or_neg(a*b)
    evm.stack.push(0 if b == 0 else abs(a) % abs(b) * sign)
    evm.pc += 1
    evm.gas_dec(5)

def addmod(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    N = evm.stack.pop()
    evm.stack.push((a+b) % N)
    evm.pc += 1
    evm.gas_dec(8)

def mulmod(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    N = evm.stack.pop()
    evm.stack.push((a + b) * N)
    evm.pc += 1
    evm.gas_dec(8)

def size_in_bytes(number):
    import math
    if number == 0: 
        return 1
    bits_needed = math.ceil(math.log2(abs(number) + 1))
    return math.ceil(bits_needed / 8)

def exp(evm):
    a, exponent = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(a ** exponent)
    evm.pc += 1
    # exp的gas成本是动态的，取决于我们需要多少字节表示指数
    evm.gas_dec(10 + (50 * size_in_bytes(exponent)))

def signextend(evm):
    b, x = evm.stack.pop(), evm.stack.pop()
    if b <= 31:
        testbit = b * 8 + 7
        sign_bit = 1 << testbit
        if x & sign_bit:
            result = x | (1**256 - sign_bit)
        else:
            result = x & (sign_bit - 1)
    else:
        result = x
    evm.stack.push(result)
    evm.pc += 1
    evm.gas_dec(5)