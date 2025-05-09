from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from translations import translations

class ChangePinWindow(QWidget):
    def __init__(self, database, language, switch_to_operation_end):
        super().__init__()
        self.database = database
        self.language = language
        self.switch_to_operation_end = switch_to_operation_end
        self.current_user = None
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.title_label = QLabel(translations[self.language]["change_pin_title"])
        self.new_pin_input = QLineEdit()
        self.new_pin_input.setPlaceholderText(translations[self.language]["change_pin_placeholder"])
        self.new_pin_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_button = QPushButton(translations[self.language]["change_pin_button"])
        self.confirm_button.clicked.connect(self.process_change_pin)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.new_pin_input)
        self.layout.addWidget(self.confirm_button)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color: #f0f0f0; font-size: 16px;")

    def set_current_user(self, card_number):
        self.current_user = card_number

    def update_language(self, language):
        self.language = language
        self.title_label.setText(translations[self.language]["change_pin_title"])
        self.new_pin_input.setPlaceholderText(translations[self.language]["change_pin_placeholder"])
        self.confirm_button.setText(translations[self.language]["change_pin_button"])

    def process_change_pin(self):
        new_pin = self.new_pin_input.text()
        if len(new_pin) >= 4:
            self.database.update_pin(self.current_user, new_pin)
            self.switch_to_operation_end(translations[self.language]["change_pin_success"])
        else:
            QMessageBox.warning(self, "Error", translations[self.language]["change_pin_invalid"])