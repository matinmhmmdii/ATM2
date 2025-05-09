from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from models.user import User
from translations import translations

class TransferWindow(QWidget):
    def __init__(self, database, language, switch_to_operation_end):
        super().__init__()
        self.database = database
        self.language = language
        self.switch_to_operation_end = switch_to_operation_end
        self.current_user = None
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.title_label = QLabel(translations[self.language]["transfer_title"])
        self.target_card_input = QLineEdit()
        self.target_card_input.setPlaceholderText(translations[self.language]["transfer_target_placeholder"])
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText(translations[self.language]["transfer_amount_placeholder"])
        self.transfer_button = QPushButton(translations[self.language]["transfer_button"])
        self.transfer_button.clicked.connect(self.process_transfer)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.target_card_input)
        self.layout.addWidget(self.amount_input)
        self.layout.addWidget(self.transfer_button)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color: #f0f0f0; font-size: 16px;")

    def set_current_user(self, card_number):
        self.current_user = card_number

    def update_language(self, language):
        self.language = language
        self.title_label.setText(translations[self.language]["transfer_title"])
        self.target_card_input.setPlaceholderText(translations[self.language]["transfer_target_placeholder"])
        self.amount_input.setPlaceholderText(translations[self.language]["transfer_amount_placeholder"])
        self.transfer_button.setText(translations[self.language]["transfer_button"])

    def process_transfer(self):
        try:
            target_card = self.target_card_input.text()
            amount = int(self.amount_input.text())
            if target_card not in self.database.users:
                QMessageBox.warning(self, "Error", translations[self.language]["transfer_not_found"])
                return
            user_data = self.database.get_user(self.current_user)
            target_data = self.database.get_user(target_card)
            user = User(self.current_user, user_data["pin"], user_data["balance"])
            if user.transfer(amount, target_data["balance"]):
                self.database.update_balance(self.current_user, user.balance)
                self.database.update_balance(target_card, target_data["balance"] + amount)
                self.switch_to_operation_end(translations[self.language]["transfer_success"].format(amount=amount, target=target_card))
            else:
                QMessageBox.warning(self, "Error", translations[self.language]["transfer_insufficient"])
        except ValueError:
            QMessageBox.warning(self, "Error", translations[self.language]["transfer_invalid"])