from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton
from translations import translations

class WelcomeWindow(QWidget):
    def __init__(self, set_language, switch_to_login):
        super().__init__()
        self.set_language = set_language
        self.switch_to_login = switch_to_login
        self.language = "fa"
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.title_label = QLabel(translations[self.language]["welcome_title"])
        self.language_combo = QComboBox()
        self.language_combo.addItems(["فارسی", "English"])
        self.language_combo.currentTextChanged.connect(self.change_language)
        self.continue_button = QPushButton(translations[self.language]["welcome_continue"])
        self.continue_button.clicked.connect(self.switch_to_login)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.language_combo)
        self.layout.addWidget(self.continue_button)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color: #f0f0f0; font-size: 16px;")

    def change_language(self, lang):
        lang_map = {"فارسی": "fa", "English": "en"}
        self.language = lang_map[lang]
        self.set_language(self.language)
        self.update_language()

    def update_language(self):
        self.title_label.setText(translations[self.language]["welcome_title"])
        self.continue_button.setText(translations[self.language]["welcome_continue"])