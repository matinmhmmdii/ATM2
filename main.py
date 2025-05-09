import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from gui.welcome import WelcomeWindow
from gui.login import LoginWindow
from gui.main_menu import MainMenuWindow
from gui.withdraw import WithdrawWindow
from gui.transfer import TransferWindow
from gui.change_pin import ChangePinWindow
from gui.operation_end import OperationEndWindow
from models.database import Database

class ATMMachine(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ATM Simulator")
        self.setGeometry(100, 100, 400, 600)
        self.database = Database()
        self.current_user = None
        self.language = "fa"
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.init_windows()

    def init_windows(self):
        self.welcome_window = WelcomeWindow(self.set_language, self.switch_to_login)
        self.login_window = LoginWindow(self.database, self.language, self.switch_to_main_menu)
        self.main_menu_window = MainMenuWindow(self.database, self.language, self.switch_to_withdraw, 
                                               self.switch_to_transfer, self.switch_to_change_pin)
        self.withdraw_window = WithdrawWindow(self.database, self.language, self.switch_to_operation_end)
        self.transfer_window = TransferWindow(self.database, self.language, self.switch_to_operation_end)
        self.change_pin_window = ChangePinWindow(self.database, self.language, self.switch_to_operation_end)
        self.operation_end_window = OperationEndWindow(self.language, self.switch_to_main_menu, self.switch_to_welcome)

        self.stacked_widget.addWidget(self.welcome_window)
        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.main_menu_window)
        self.stacked_widget.addWidget(self.withdraw_window)
        self.stacked_widget.addWidget(self.transfer_window)
        self.stacked_widget.addWidget(self.change_pin_window)
        self.stacked_widget.addWidget(self.operation_end_window)

        self.stacked_widget.setCurrentWidget(self.welcome_window)

    def set_language(self, lang):
        self.language = lang
        self.update_language()

    def update_language(self):
        self.login_window.update_language(self.language)
        self.main_menu_window.update_language(self.language)
        self.withdraw_window.update_language(self.language)
        self.transfer_window.update_language(self.language)
        self.change_pin_window.update_language(self.language)
        self.operation_end_window.update_language(self.language)

    def switch_to_login(self):
        self.stacked_widget.setCurrentWidget(self.login_window)

    def switch_to_main_menu(self, card_number):
        self.current_user = card_number
        self.main_menu_window.set_current_user(card_number)
        self.stacked_widget.setCurrentWidget(self.main_menu_window)

    def switch_to_withdraw(self):
        self.withdraw_window.set_current_user(self.current_user)
        self.stacked_widget.setCurrentWidget(self.withdraw_window)

    def switch_to_transfer(self):
        self.transfer_window.set_current_user(self.current_user)
        self.stacked_widget.setCurrentWidget(self.transfer_window)

    def switch_to_change_pin(self):
        self.change_pin_window.set_current_user(self.current_user)
        self.stacked_widget.setCurrentWidget(self.change_pin_window)

    def switch_to_operation_end(self, message):
        self.operation_end_window.set_message(message)
        self.stacked_widget.setCurrentWidget(self.operation_end_window)

    def switch_to_welcome(self):
        self.current_user = None
        self.stacked_widget.setCurrentWidget(self.welcome_window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    atm = ATMMachine()
    atm.show()
    sys.exit(app.exec())