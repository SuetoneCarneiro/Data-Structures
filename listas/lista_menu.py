class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class ListaEncadeada:
    def __init__(self):
        self.head: Node = None
        self._size = 0
    
    @property
    def empty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def __str__(self):
        node = self.head
        s = '['
        for i in range(self._size):
            s += str(node.value)
            if i < self._size - 1:
                s += ', '
            node = node.next
        s += ']'
        return s
    
    def __setitem__(self):
        ...

    def __getitem__(self):
        ...
    
    def append(self, value):
        new_node = Node(value)
        if self.head:
            pointer = self.head # starts with a reference to the list head
            while(pointer.next): # Complexity: O(N)
                pointer = pointer.next
            pointer.next = new_node
        else:
            self.head = new_node
        self._size += 1

    def _get_node(self, index):
        pointer = self.head
        for _ in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError()
        return pointer

    def insert(self, index, value):
        new_node = Node(value)
        if self.empty:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index > self._size:
            pointer = self.head # starts with a reference to the list head
            while(pointer.next): # Complexity: O(N)
                pointer = pointer.next
            pointer.next = new_node
        else:
            pointer = self._get_node(index - 1)
            new_node.next = pointer.next
            pointer.next = new_node
        self._size += 1

    def remove(self, index):
        ...
    

if __name__ == '__main__':
    lista = ListaEncadeada()
    print(lista.empty)
    for i in range(11):
        lista.append(i)
    lista.insert(0, 88)
    lista.insert(1000, 0)
    print(lista)
 