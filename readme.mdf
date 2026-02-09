# Bank Account Management System

A Python-based Command Line Interface (CLI) application that simulates a simple banking system. This application allows users to create accounts, manage transactions, and update user information, with all data persisted locally using a JSON file.

## 📋 Features

* **Account Creation**: Create a new bank account with validation (Age verification, valid email check, and 4-digit PIN).
* **Unique ID Generation**: Automatically generates a secure, randomized alphanumeric Account ID.
* **Deposit Money**: Add funds to your account (includes limits checking).
* **Withdraw Money**: Withdraw funds (includes sufficient balance checking).
* **View Details**: Check current balance and account profile.
* **Update Information**: Modify Name, Email, or PIN (sensitive fields like Age and Balance are protected).
* **Delete Account**: Remove an account permanently from the database.
* **Persistent Storage**: All data is saved automatically to `data.json`, ensuring data remains after the program closes.

## 🛠️ Prerequisites

* Python 3.x installed on your machine.
* No external libraries are required (uses standard `json`, `random`, `string`, and `pathlib` libraries).

## 🚀 Getting Started

1.  **Download the files**
    Ensure you have `main.py` and `data.json` in the same directory.

2.  **Run the Application**
    Open your terminal or command prompt, navigate to the project directory, and run:

    ```bash
    python main.py
    ```

3.  **Using the System**
    Follow the on-screen menu prompts to navigate the system:
    * Enter `1` to create an account. **Important:** Note down the generated Account ID!
    * Enter `2` or `3` to perform transactions using your Account ID and PIN.
    * Enter `7` to save and exit safely.

## 📂 File Structure

* `main.py`: The core application script containing the `Bank` class and the main execution loop.
* `data.json`: The database file where user accounts are stored in JSON format.

## 🔒 Validations

The system enforces specific rules for data integrity:
* **PIN**: Must be exactly 4 digits.
* **Age**: User must be 18 years or older.
* **Email**: Must contain an '@' symbol.
* **Deposit Limit**: Single transaction cannot exceed 100,000.

## 📝 Usage Example

```text
--- Bank Account Management System ---

 press 1 to create a new account
 press 2 to deposit money
 ...
 Enter your choice: 1
 Enter your name: John Doe
 Enter your age: 25
 ...
 Your account has been created successfully.
 account_number : A1B@2C (Save this!)