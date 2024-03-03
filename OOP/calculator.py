import os

class Calculator:
    def __init__(self, register={'last_value' : 0, 'current_value' : 0}):
        self._register = register
    
    # This method also can be made with '@property'
    def get_register(self, search):
        if search == 'last_value' or search == 'undo':
            return self._register['last_value']
        else:
            return self._register['current_value']

    def reset_register(self):
        self._register = {'last_value' : 0, 'current_value' : 0}

    def sum(self, value):
        self._register['last_value'] = self._register['current_value']
        result = self._register['current_value'] + value
        self._register['current_value'] = result
        return result
    
    def subtraction(self, value):
        self._register['last_value'] = self._register['current_value']
        result = self._register['current_value'] - value
        self._register['current_value'] = result
        return result
    
    def multiply(self, value):
        self._register['last_value'] = self._register['current_value']
        result = self._register['current_value'] * value
        self._register['current_value'] = result
        return result
    
    def divide(self, value):
        self._register['last_value'] = self._register['current_value']
        result = self._register['current_value'] / value
        self._register['current_value'] = result
        return result

    def __str__(self) -> str:
        return f">> Resgister\nCurrent Value: {self.get_register('current_value')}\nLast Value: {self.get_register('last_value')}"

