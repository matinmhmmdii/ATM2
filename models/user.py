class User:
    def __init__(self, card_number, pin, balance):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer(self, amount, target_user_balance):
        if self.withdraw(amount):
            target_user_balance += amount
            return True
        return False

    def change_pin(self, new_pin):
        self.pin = new_pin