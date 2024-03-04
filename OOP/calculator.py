import os
from time import sleep

class Calculator:
    def __init__(self, register={'last_value' : 0, 'current_value' : 0}):
        self._register = register
    
    # This method also can be made with '@property'
    def get_register(self, search):
        if search == 'last_value':
            return self._register['last_value']
        elif search == 'current_value':
            return self._register['current_value']
        else:
            self._register['current_value'] = self._register['last_value']
            return self._register['current_value']

    def reset_register(self):
        self._register = {'last_value' : 0, 'current_value' : 0}

    def sum(self, value):
        self._register['last_value'] = self._register['current_value']
        self._register['current_value'] += value
        return self._register['current_value']
    
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

class GraphicalCalculator:
    def __init__(self):
        self.calc = Calculator()
        self.menu()

    def menu(self):

        while True:
            calc_design = '''

        +--------------+
        |          {:.2f}|
        +--------------+
        (+) sum
        (-) subtract
        (/) divide
        (*) multiply
        (r) reset
        (u) undo
        (e) exit
        ----------------- 
        '''.format(self.calc.get_register('current_value'))
            os.system('clear')
            print(calc_design, end='')
            operation = input('Operation: ')
            if operation == 'e':
                break

            if operation in '+-*/':
                try:
                    value = int(input('\tValue: '))
                except ValueError:
                    print('\t\033[0;49;31mInvalid value. Try again\033[m')
                    sleep(3)
                    continue
            else:
                pass
            
            match operation:
                case '+':
                    self.calc.sum(value)
                case '-':
                    self.calc.subtraction(value)
                case '*':
                    self.calc.multiply(value)
                case '/':
                    self.calc.divide(value)
                case 'r':
                    self.calc.reset_register()
                case 'u':
                    self.calc.get_register('undo')
                case _ :
                    print(f'\t\033[0;49;31mInvalid Operation\033[m')
                    sleep(3)

my_calculator = GraphicalCalculator()
