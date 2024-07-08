class Array:

    def __init__(self, length):
        self.lenght = length
        self._data = [None]*length

    def set(self, position: int, value):
        self._data[position] = value
    
    def __setitem__(self, position: int, value):
        self.set(position, value)
     
    def get(self, position: int):
        return self._data[position]
    
    def __getitem__(self, position: int):
        return self.get(position)
    
    
    