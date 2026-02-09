# Bank Account Management System
    #1. bank account create
    #2. deposit money
    #3. withdraw money
    #4. view details
    #5. update details
    #6. delete account
    #7. exit

# data will be saved in json file
# when first time class runs, dummy data will be created in json file, then we will read and write data from json file
# data.json -> dummy -> update -> data.json
import json
import random
import string
from pathlib import Path

class Bank:
    database = Path("data.json")
    data = [] #dummy data

    try:
        if Path(database).exists():
            with open(database, "r") as fs:
                data = json.load(fs)
        else:
            print("no such file exists.")
    except Exception as err:
        print(f"Error occured {err}")

    @classmethod
    def __update(cls): # dummy data will be updated in json file
        with open(cls.database, "w") as fs:
            fs.write(json.dumps(cls.data, indent=4))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_uppercase, k=3)
        num = random.choices(string.digits, k=3)
        spchars = random.choices("!@#$%^&*()_+", k=1)

        id = alpha + num + spchars
        random.shuffle(id)
        return "".join(id)

    def create_account(self):
        info = {
            "name" : input("Enter your name: "),
            "age" : int(input("Enter your age: ")),
            "email" : input("Enter your email: "),
            "pin" : input("Enter your 4 digit pin: "),
            "account_number" : Bank.__accountgenerate(),
            "balance" : 0
        } # information is taken from user

        if len(info["pin"]) != 4 or info["age"] < 18 or "@" not in info["email"] or info["pin"].isdigit() == False:
            print("Sorry. Your account cannot be created. Please check your details and try again.")
        else:
            print("\n Your account has been created successfully.")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number.")

            Bank.data.append(info) # user information is added to dummy data
            Bank.__update()

    def deposit_money(self):
        acc_num = input("Enter your account number: ")
        pin = input("Enter your 4 digit pin: ")

        userdata = [i for i in Bank.data if i["account_number"] == acc_num and i["pin"] == pin] #deepcopy. thats why below changin deepcopy also make changes in the dummy data.

        if bool(userdata) == False:
            print("Invalid account number or pin. Account not found. Please try again.")
        else:
            amount = int(input("Enter the amount you want to deposit: "))
            if amount <= 0:
                print("Invalid amount. Please enter a positive number.")
            elif amount >= 100000:
                print("Amount exceeds the maximum limit of 100000. Please enter a valid amount.")
            else:
                userdata[0]["balance"] += amount
                Bank.__update()
                print(f"Amount deposited successfully. Your new balance is: {userdata[0]['balance']}") 
    
    def withdraw_money(self):
        acc_num = input("Enter your account number: ")
        pin = input("Enter your 4 digit pin: ")

        userdata = [i for i in Bank.data if i["account_number"] == acc_num and i["pin"] == pin] #deepcopy. thats why below changin deepcopy also make changes in the dummy data.

        if bool(userdata) == False:
            print("Invalid account number or pin. Account not found. Please try again.")
        else:
            amount = int(input("Enter the amount you want to withdraw : "))
            if userdata[0]["balance"] < amount:
                print(f"Insufficient balance. Your current balance is: {userdata[0]['balance']}")
            else:
                userdata[0]["balance"] -= amount
                Bank.__update()
                print(f"Amount withdrawn successfully. Your new balance is: {userdata[0]['balance']}")

    def view_details(self):
        acc_num = input("Enter your account number: ")
        pin = input("Enter your 4 digit pin: ")

        userdata = [i for i in Bank.data if i["account_number"] == acc_num and i["pin"] == pin]

        if bool(userdata) == False:
            print("Invalid account number or pin. Account not found. Please try again.")
        else:
            print("Your Account Details are: \n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def update_details(self):
        acc_num = input("Enter your account number: ")
        pin = input("Enter your 4 digit pin: ")

        userdata = [i for i in Bank.data if i["account_number"] == acc_num and i["pin"] == pin]
        
        if bool(userdata) == False:
            print("Invalid account number or pin. Account not found. Please try again.")
        else:
            print("You cannot update age, account number and balance. You can update only name, email and pin.")
            print("fill the details you want to update and leave the rest blank (press enter).")
            
            newdata = {
                "name" : input("Enter your new name: "),
                "email" : input("Enter your new email: "),
                "pin" : input("Enter your new 4 digit pin: "),
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]
            newdata["age"] = userdata[0]["age"]
            newdata["account_number"] = userdata[0]["account_number"]
            newdata["balance"] = userdata[0]["balance"]

            if newdata["pin"].isdigit() == False or len(newdata["pin"]) != 4 or "@" not in newdata["email"]:
                print("You entered invalid details. Please check your details and try again.")
                return

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("Your details have been updated successfully. Your new details are: \n")

    def delete_account(self):
        acc_num = input("Enter your account number: ")
        pin = input("Enter your 4 digit pin: ")

        userdata = [i for i in Bank.data if i["account_number"] == acc_num and i["pin"] == pin]

        if bool(userdata) == False:
            print("Invalid account number or pin. Account not found. Please try again.")
        else:
            confirm = input("Are you sure you want to delete your account? This action cannot be undone. Enter 'Y' to confirm or 'N' to cancel: ")
            if confirm.upper() == "Y":
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.__update()
                print("Your account has been deleted successfully. We're sorry to see you go!")
            elif confirm.upper() == "N":
                print("Account deletion cancelled. Your account is safe.")
            else:
                print("Invalid input. Bypassed account deletion. Your account is safe.")
            


user = Bank()

print("--- Bank Account Management System ---")

while True:
    print("\n press 1 to create a new account")
    print(" press 2 to deposit money")
    print(" press 3 to withdraw money")
    print(" press 4 to view account details")
    print(" press 5 to update account details")
    print(" press 6 to delete account")
    print(" press 7 to exit \n")
    try:
        check = int(input("Enter your choice: "))
        if check == 1:
            user.create_account()
        elif check == 2:
            user.deposit_money()
        elif check == 3:
            user.withdraw_money()
        elif check == 4:
            user.view_details()
        elif check == 5:
            user.update_details()
        elif check == 6:
            user.delete_account()
        elif check == 7:
            print("Thank you for using the Bank Account Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    except Exception as err:
        print(f"Error occured: {err}. Please enter a valid choice.")