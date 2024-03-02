class CurrentAccount:
    def __init__(self, number, balance, name):
        self._number = number
        self._balance = balance
        self._name = name

    # Gets -----------------------------------------
    @property
    def number(self):
        return self._name
        
    @property 
    def balance(self):
        return self._balance
    
    @property
    def name(self):
        return self._name
    # --------------------------------------------------

    # Sets
    @balance.setter
    def withdraw(self, withdraw_value): # return bool: true if there is money enough and false if there isn't
        if withdraw_value >= self._balance:
            self._balance -= withdraw_value
            return True
        else:
            return False
        
    def make_deposit(self, deposit_value): # Doesn't have 'return', just increase the balance
        self.balance += deposit_value

    def name(self, new_name):
        self._name = new_name
    