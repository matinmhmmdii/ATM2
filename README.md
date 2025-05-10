# ATM Simulator

A simple ATM simulator built using PyQt6 for the Advanced Programming course. This project provides a GUI-based interface to simulate basic ATM functionalities with support for Persian and English languages.

## Features

- Welcome page with language selection (Persian/English)
- Login with card number and PIN
- Main menu to check balance, withdraw, transfer, or change PIN
- Support for withdrawal, transfer, and PIN change operations
- Operation end page with options to continue or exit
- Data persistence using a JSON file
- Modular code following OOP and Clean Code principles

## Requirements

- Python 3.8 or higher
- PyQt6

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/matinmhmmdii/ATM2
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:

   ```bash
   python main.py
   ```

## Usage

- Select a language (Persian or English) on the welcome page.
- Log in using one of the sample accounts:
  - Card Number: `123456789`, PIN: `1234`
  - Card Number: `987654321`, PIN: `4321`
- Navigate through the main menu to perform operations.
- User data (balance, PIN) is saved in `users.json`.

## Project Structure

```
ATM-Project/
├── main.py
├── translations.py
├── gui/
│   ├── __init__.py
│   ├── welcome.py
│   ├── login.py
│   ├── main_menu.py
│   ├── withdraw.py
│   ├── transfer.py
│   ├── change_pin.py
│   ├── operation_end.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── database.py
├── README.md
├── requirements.txt
```

## 
