
MAXIMUM_STACK_SIZE = 1024

class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def __str__(self) -> str:
        ws = []
        for i, item in enumerate(self.items[::-1]):
            if i == 0:
                ws.append(f"{item} < first")
            elif i == len(self.items) -1:
                ws.append(f"{item} < last")
            else:
                ws.append(str(item))
        return "\n".join(ws)

    def push(self, value):
        if len(self.items) == MAXIMUM_STACK_SIZE - 1:
            raise Exception("Stack overflow")
        
        self.items.append(value)
    
    def pop(self, n=-1):
        if len(self.items) < n:
            raise Exception("Stack overflow")
        value = self.items[n]
        del self.items[n]
        return value

if __name__ == '__main__':
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push(1)
    print(stack)
    print('-' * 20)
    stack.pop()
    print(stack)