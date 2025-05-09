from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from translations import translations

class OperationEndWindow(QWidget):
    def __init__(self, language, switch_to_main_menu, switch_to_welcome):
        super().__init__()
        self.language = language
        self.switch_to_main_menu = switch_to_main_menu
        self.switch_to_welcome = switch_to_welcome
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.message_label = QLabel("")
        self.new_operation_button = QPushButton(translations[self.language]["operation_end_new_operation"])
        self.exit_button = QPushButton(translations[self.language]["operation_end_exit"])
        self.new_operation_button.clicked.connect(self.switch_to_main_menu)
        self.exit_button.clicked.connect(self.switch_to_welcome)
        self.layout.addWidget(self.message_label)
        self.layout.addWidget(self.new_operation_button)
        self.layout.addWidget(self.exit_button)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color: #f0f0f0; font-size: 16px;")

    def set_message(self, message):
        self.message_label.setText(message)

    def update_language(self, language):
        self.language = language
        self.new_operation_button.setText(translations[self.language]["operation_end_new_operation"])
        self.exit_button.setText(translations[self.language]["operation_end_exit"])