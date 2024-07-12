from array_ifpb import Array

class Stack:
    def __init__(self):
        ...
    
    def push(self, element):
        ...
    
    def pop(self):
        ...
    
    def show(self):
        ...
    
    @property
    def top(self):
        ...

class EasyStack:
    def __init__(self):
        self._data = []
    
    def push(self, element):
        self._data.append(element)

    def pop(self):
        return self._data.pop()
    
    def show(self):
        for element in self._data:
            print(element, end=' ')
        print()
    
    @property
    def top(self):
        return self._data[-1]
    

class EmptyStack(Exception):
    pass


class FullStack(Exception):
    pass


class SequencialStack(Stack):
    def __init__(self):
        self._data = Array(length=3)
        self._top = 0

    @property
    def top(self):
        if self.is_empty:
            raise EmptyStack()
        return self._data.get(self._top - 1)
    
    @property
    def len(self):
        return self._top

    @property
    def is_empty(self):
        return self.len == 0
    
    @property
    def is_full(self):
        return self.len == self._data.lenght
    
    def _resize(self):
        old_data = self._data
        new_data = Array(old_data.lenght * 2)
        self._data = new_data
        self._data.copy_from(old_data)


    def push(self, element):
        if self.is_full:
            self._resize()

        self._data.set(self._top, element)
        self._top += 1
    

    def pop(self):
        if self.is_empty:
            raise EmptyStack()
        
        top = self.top
        self._top -= 1
        self._data.set(self._top, None)
        return top
    
    def show(self):
        for i in range(self._top):
            print(self._data.get(i), end=' ')
        print()
    

def sequencial_stack_test():
    stack = SequencialStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.show()
    assert stack.pop() == 3
    assert stack.top == 3
    stack.show()
    assert stack.is_full == False


if __name__ == '__main__':
    sequencial_stack_test()

