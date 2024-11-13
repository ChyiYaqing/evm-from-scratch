"""
字节码由指令和数据组成
"""
from pkg.stack import stack
from pkg.memory import memory
from pkg.storage import storage
from pkg.op import opCode, opStop, opMath, opPush

class EVM:
    def __init__(self, program, gas, value, calldata = []) -> None:
        self.pc = 0
        self.stack = stack.Stack()
        self.memory = memory.Memory()
        self.storage = storage.Storage()

        self.program = program
        self.gas = gas
        self.value = value
        self.calldata = calldata

        self.stop_flag = False
        self.revert_flag = False

        self.returndata = []
        self.logs = []
    
    def peek(self):
        return self.program[self.pc]
    
    def gas_dec(self, amount):
        if self.gas - amount < 0:
            raise Exception("out of gas")
        self.gas -= amount
    
    def should_execute_next_opcode(self):
        if self.pc > len(self.program) -1:
            return False
        if self.stop_flag:
            return False
        if self.revert_flag:
            return False

        return True

    def run(self):
        while self.should_execute_next_opcode():
            op = self.program[self.pc]
            if op == opCode.STOP: 
                opStop.stop(self)
            if op == opCode.ADD:
                opMath.add(self)
            if op == opCode.MUL:
                opMath.mul(self)
            if op == opCode.PUSH1:
                opPush._push(self,1)
    
    def reset(self):
        self.pc = 0
        self.stack = stack.Stack()
        self.memory = memory.Memory()
        self.storage = storage.Storage()

if __name__ == "__main__":
    SIMPLE_ADD = [0x60, 0x42, 0x60, 0xFF, 0x01]
    evm = EVM(SIMPLE_ADD, 100000, 10, [])
    evm.run()
    print(evm.stack)