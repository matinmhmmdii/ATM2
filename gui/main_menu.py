from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from translations import translations

class MainMenuWindow(QWidget):
    def __init__(self, database, language, switch_to_withdraw, switch_to_transfer, switch_to_change_pin):
        super().__init__()
        self.database = database
        self.language = language
        self.switch_to_withdraw = switch_to_withdraw
        self.switch_to_transfer = switch_to_transfer
        self.switch_to_change_pin = switch_to_change_pin
        self.current_user = None
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.title_label = QLabel(translations[self.language]["main_menu_title"])
        self.balance_label = QLabel(translations[self.language]["main_menu_balance"].format(balance=0))
        self.withdraw_button = QPushButton(translations[self.language]["main_menu_withdraw"])
        self.transfer_button = QPushButton(translations[self.language]["main_menu_transfer"])
        self.change_pin_button = QPushButton(translations[self.language]["main_menu_change_pin"])
        self.withdraw_button.clicked.connect(self.switch_to_withdraw)
        self.transfer_button.clicked.connect(self.switch_to_transfer)
        self.change_pin_button.clicked.connect(self.switch_to_change_pin)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.balance_label)
        self.layout.addWidget(self.withdraw_button)
        self.layout.addWidget(self.transfer_button)
        self.layout.addWidget(self.change_pin_button)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color: #f0f0f0; font-size: 16px;")

    def set_current_user(self, card_number):
        self.current_user = card_number
        user_data = self.database.get_user(card_number)
        self.balance_label.setText(translations[self.language]["main_menu_balance"].format(balance=user_data["balance"]))

    def update_language(self, language):
        self.language = language
        self.title_label.setText(translations[self.language]["main_menu_title"])
        self.withdraw_button.setText(translations[self.language]["main_menu_withdraw"])
        self.transfer_button.setText(translations[self.language]["main_menu_transfer"])
        self.change_pin_button.setText(translations[self.language]["main_menu_change_pin"])
        if self.current_user:
            user_data = self.database.get_user(self.current_user)
            self.balance_label.setText(translations[self.language]["main_menu_balance"].format(balance=user_data["balance"]))