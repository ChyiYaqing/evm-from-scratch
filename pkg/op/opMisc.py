"""
预编译
    以太坊中的预编译是EVM可以直接执行的程序。目前有9个,在EVM字节码中实现这些函数会非常耗费gas, 
    因此我们决定将他们包含在EVM本身中。

Address:    Name:           MINIMUM GAS:    DESCRIPTION: 
0x01        ecRecover       3000            Elliptic curve digital signature algorithm (ECDSA) public key recovery function.
0x02        SHA2-256        60              Hash function
0x03        RPIEMD-160      600             Hash function
0x04        identity        15              Returns the input
0x05        modexp          200             Arbitrary-precision exponentiation under modulo
0x06        exAdd           150             Point addition (ADD) on the elliptic curve 'alt_bn128'
0x07        ecMul           6000            Scalar multiplication (MUL) on the elliptic curve 'alt_bn128'
0x08        ecPairing       45000           Bilinear function on groups on the elliptic curve 'alt_bn128'
0x09        blake2f         0               Compression function F used in the BLAKE2 cryptographic hashing algorithm
"""

"""
哈希
    哈希函数是最重要的加密原语之一，它具有以下特点:
        固定大小： 每个输入(也称为消息)都会创建一个固定大小的哈希值
        确定性: 相同的输入每次都会产生相同的输出
        单向: 实际上不可能逆转
        混乱: 只要有一个位发生变化，整个哈希值就会以完全混乱和随机的方式发生变化
"""

def sha3(evm): # EVM使用Keccak-256函数
    offset, size = evm.stack.pop(), evm.stack.pop()
    value = evm.memory.access(offset, size)
    evm.stack.push(hash(str(value)))

    evm.pc += 1

    # calculate gas
    minimum_word_size = (size + 31) / 32
    dynamic_gas = 6 * minimum_word_size # TODO: + memory_expansion_cost
    evm.gas_dec(30 + dynamic_gas)