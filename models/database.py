import json

class Database:
    def __init__(self, file_path="users.json"):
        self.file_path = file_path
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            default_users = {
                "123456789": {"pin": "1234", "balance": 1000000},
                "987654321": {"pin": "4321", "balance": 500000}
            }
            self.save_users(default_users)
            return default_users

    def save_users(self, users=None):
        if users is None:
            users = self.users
        with open(self.file_path, 'w') as file:
            json.dump(users, file, indent=4)

    def add_user(self, card_number, pin, balance):
        self.users[card_number] = {"pin": pin, "balance": balance}
        self.save_users()

    def get_user(self, card_number):
        return self.users.get(card_number)

    def update_balance(self, card_number, balance):
        if card_number in self.users:
            self.users[card_number]["balance"] = balance
            self.save_users()

    def update_pin(self, card_number, new_pin):
        if card_number in self.users:
            self.users[card_number]["pin"] = new_pin
            self.save_users()