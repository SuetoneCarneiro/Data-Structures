from array_ifpb import Array

class Stack:
    def __init__(self):
        ...
    
    def stack_up(self, element):
        ...
    
    def unstack(self):
        ...
    
    def show(self):
        ...
    
    @property
    def top(self):
        ...

class EasyStack:
    def __init__(self):
        self._data = []
    
    def stack_up(self, element):
        self._data.append(element)

    def unstack(self):
        return self._data.pop()
    
    def show(self):
        for element in self._data:
            print(element, end=' ')
        print()
    
    @property
    def top(self):
        return self._data[-1]
    

class SequencialStack(Stack):
    def __init__(self):
        self._data = Array(length=10)
        self._top = 9
    
    def stack_up(self, element):
        self._data[self._top - 1] = self._data[self._top]
        self._data.set(self._top, element)
    
    #FIX ME:
    def unstack(self):
        self._data.set(self._top, None)
    
    def show(self):
        for i in range(10):
            print(self._data.get(i), end=' ')
    
    @property
    def top(self):
        return self._data.get(self._top)

def sequencial_stack_test():
    stack = SequencialStack()
    stack.stack_up(1)
    stack.stack_up(2)
    stack.show()
    assert stack.top == 2


if __name__ == '__main__':
    sequencial_stack_test()

