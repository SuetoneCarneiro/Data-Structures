class CurrentAccount:
    def __init__(self, name, number, balance):
        self._name = name
        self._number = number
        self._balance = balance

    # Gets -----------------------------------------
    @property
    def number(self):
        return self._number
        
    @property 
    def balance(self):
        return self._balance
    
    @property
    def name(self):
        return self._name
    # --------------------------------------------------

    # Sets
    @name.setter
    def change_name(self, new_name):
        self._name = new_name

    #Methods 
    def withdraw(self, withdraw_value): # return bool: true if there is money enough and false if there isn't
        if self._balance >= withdraw_value:
            self._balance -= withdraw_value
            return True
        else:
            return False
    
    def make_deposit(self, deposit_value): # Doesn't have 'return', just increase the balance
        self._balance += deposit_value
    
    def __str__(self) -> str:
        return f'Name: {self.name}\nNumber: {self.number}\nBalance: ${self.balance}'

# Tests area 

name = str(input('Name of the owner of the bank account: '))
number = int(input('Account number: '))
balance = int(input('Initial balance: $ '))

account_demo = CurrentAccount(name, number, balance)

while True:
    print('\n-------Menu-------')
    print('[1] Make a deposit\n[2] Withdraw\n[3] Check balance\n[4] Exit')
    op = int(input('>>> '))
    if op == 4: 
        break

    if op == 1:
        value = int(input('Deposit value: $'))
        account_demo.make_deposit(value)

    if op == 2:
        value = int(input('Withdraw value: $'))
        if not account_demo.withdraw(value):
            print('Insufficient balance')
        else:
            print('Successful withdrawal')
    
    if op == 3:
        print(f'Your balance: ${account_demo.balance}')
    
