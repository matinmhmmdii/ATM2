from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from translations import translations

class LoginWindow(QWidget):
    def __init__(self, database, language, switch_to_main_menu):
        super().__init__()
        self.database = database
        self.language = language
        self.switch_to_main_menu = switch_to_main_menu
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.title_label = QLabel(translations[self.language]["login_title"])
        self.card_input = QLineEdit()
        self.card_input.setPlaceholderText(translations[self.language]["login_card_placeholder"])
        self.pin_input = QLineEdit()
        self.pin_input.setPlaceholderText(translations[self.language]["login_pin_placeholder"])
        self.pin_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton(translations[self.language]["login_button"])
        self.login_button.clicked.connect(self.check_login)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.card_input)
        self.layout.addWidget(self.pin_input)
        self.layout.addWidget(self.login_button)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color: #f0f0f0; font-size: 16px;")

    def update_language(self, language):
        self.language = language
        self.title_label.setText(translations[self.language]["login_title"])
        self.card_input.setPlaceholderText(translations[self.language]["login_card_placeholder"])
        self.pin_input.setPlaceholderText(translations[self.language]["login_pin_placeholder"])
        self.login_button.setText(translations[self.language]["login_button"])

    def check_login(self):
        card_number = self.card_input.text()
        pin = self.pin_input.text()
        user_data = self.database.get_user(card_number)
        if user_data and user_data["pin"] == pin:
            self.switch_to_main_menu(card_number)
        else:
            QMessageBox.warning(self, "Error", translations[self.language]["login_error"])