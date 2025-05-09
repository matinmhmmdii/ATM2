from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from models.user import User
from translations import translations

class WithdrawWindow(QWidget):
    def __init__(self, database, language, switch_to_operation_end):
        super().__init__()
        self.database = database
        self.language = language
        self.switch_to_operation_end = switch_to_operation_end
        self.current_user = None
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.title_label = QLabel(translations[self.language]["withdraw_title"])
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText(translations[self.language]["withdraw_amount_placeholder"])
        self.withdraw_button = QPushButton(translations[self.language]["withdraw_button"])
        self.withdraw_button.clicked.connect(self.process_withdraw)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.amount_input)
        self.layout.addWidget(self.withdraw_button)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color: #f0f0f0; font-size: 16px;")

    def set_current_user(self, card_number):
        self.current_user = card_number

    def update_language(self, language):
        self.language = language
        self.title_label.setText(translations[self.language]["withdraw_title"])
        self.amount_input.setPlaceholderText(translations[self.language]["withdraw_amount_placeholder"])
        self.withdraw_button.setText(translations[self.language]["withdraw_button"])

    def process_withdraw(self):
        try:
            amount = int(self.amount_input.text())
            user_data = self.database.get_user(self.current_user)
            user = User(self.current_user, user_data["pin"], user_data["balance"])
            if user.withdraw(amount):
                self.database.update_balance(self.current_user, user.balance)
                self.switch_to_operation_end(translations[self.language]["withdraw_success"].format(amount=amount))
            else:
                QMessageBox.warning(self, "Error", translations[self.language]["withdraw_insufficient"])
        except ValueError:
            QMessageBox.warning(self, "Error", translations[self.language]["withdraw_invalid"])