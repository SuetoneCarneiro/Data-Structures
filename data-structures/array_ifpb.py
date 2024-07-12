class Array:

    def __init__(self, length: int):
        self.lenght = length
        self._data = [None]*length


    def position_check(self, position):
        if not position >= 0:
            raise IndexError('Invalid position')
        
    def set(self, position: int, value):
        if not position >= 0:
            raise IndexError('Invalid position')
        self._data[position] = value
    
    def __setitem__(self, position: int, value):
        self.set(position, value)
     
    def get(self, position: int):
        return self._data[position]
    
    def __getitem__(self, position: int):
        return self.get(position)
    
    def copy_from(self, another_array):
        for i in range(another_array.len):
            self.set(i, another_array.get(i))
    