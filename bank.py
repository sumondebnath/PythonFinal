from abc import ABC, abstractmethod

class Bank(ABC):
    userAcc = []
    bankBalance = 0
    totalloan = 0
    loanFeature = True
    isBankrupt = False

    def __init__(self, name, email, address, password, accType) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.accType = accType
        self.accNumber = User.get_accNumber(self)

        self.balance = 0
        Bank.userAcc.append(self)

        self.history = []
        self.loan = 2 

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"{self.name} Deposit {amount}.\n")
        else:
            print("Diposit amount not Acceptable\n")
    
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else :
            print("Withdrawal amount exceeded\n")

    def get_balance(self):
        print(self.balance)

    def histories(self):
        for hist in self.history:
            print(hist)


class Admin(Bank):
    def __init__(self, name, email, address, password, accType) -> None:
        super().__init__(name, email, address, password, accType)

    def deleteUser(self, name):
        for user in Bank.userAcc:
            if user.name == name:
                Bank.userAcc.remove(user) 

    def showUser(self):
        for user in Bank.userAcc:
            print(f"Name: {user.name} Email: {user.email} Address: {user.address} Account Number: {user.accNumber} Account: {user.accType}")
        print()

    def getBankBalance(self):
        print(f"Total Bank Balance : {Bank.bankBalance}\n")

    def get_loan(self):
        print(f"Total Bank Loan : {Bank.totalloan}\n")

    def loan_feature(self):
        Bank.loanFeature = False
        print("Loan Feature OFF.\n")
    
    def bankrupt(self):
        Bank.isBankrupt = True
        print("\nThe Bank Is Bankrupt.\n")


class User(Bank):
    def __init__(self, name, email, address, password, accType) -> None:
        super().__init__(name, email, address, password, accType)

    def deposit(self, amount):
        if self.isBankrupt == False:
            if amount >= 0:
                self.balance += amount
                self.history.append(f"{self.name} Deposit {amount}.")
            else :
                print("Not Enough Money.")
        else :
            print("\nThe Bank Is Bankrupt.\n")
    
    def withdraw(self, amount):
        if self.isBankrupt == False:
            if amount < self.balance:
                self.balance -= amount
                self.history.append(f"{self.name} withdraw {amount}")
            else:
                print("Withdrawal amount exceeded\n")
        else :
            print("\nThe Bank Is Bankrupt.\n")

    def get_balance(self):
        if self.isBankrupt == False:
            print(self.balance)
        else :
            print("\nThe Bank Is Bankrupt.\n")

    def histories(self):
        if self.isBankrupt == False:
            for hist in self.history:
                print(hist)
            print()
        else :
            print("\nThe Bank Is Bankrupt.\n")

    def get_accNumber(self):
        # accNumber = self.name + self.address
        return self.name + self.address
    
    def take_loan(self, amount):
        if self.isBankrupt == False:
            if Bank.loanFeature == True:
                if self.loan != 0:
                    self.balance += amount
                    Bank.totalloan += amount
                    self.loan -= 1
                    self.history.append(f"{self.name} Get loan {amount}")
                else :
                    print("Bank Loan Limit gone.\n")
            else:
                print("Loan Feature Not Available.\n")
        else :
            print("\nThe Bank Is Bankrupt.\n")
        
    def transfer_amount(self, name, amount):
        if self.isBankrupt == False:
            if amount < self.balance:
                for user in Bank.userAcc:
                    if user.name == name:
                        self.balance -= amount
                        self.history.append(f"{self.name} Transfer Money {amount} to {name}")
                    else:
                        print("Account does not exist\n")
                        return
            else:
                print(f"{amount} dose not exist.\n")
        else :
            print("\nThe Bank Is Bankrupt.\n")
    

admin = Admin("admin", "admin.com", "512A", "1234", None)

currentuser = None

while True:
    if currentuser == None:
        print("No User logged In.")
        print()
        print("1. Admin.")
        print("2. User.")
        print()

        ch = int(input("Enter: "))
        if ch == 1:
            chh = input("Register or Login (L/R): ")
            if chh == "R" or chh=="r":
                name = input("Enter name: ")
                password = input("Enter Password: ")
                email = input("Enter Email: ")
                address = input("Enter Address: ")
                accType = input("Enter Account Type: ")
                currentuser = Admin(name, email, address, password, accType)
        

            elif chh=="L" or chh=="l":
                name = input("Enter name: ")
                password = input("Enter Password: ")

                for user in Bank.userAcc:
                    if user.name == name and user.password == password:
                        currentuser = user
                        break
        
        else:
            chh = input("Register or Login (L/R): ")
            if chh == "R" or chh=="r":
                name = input("Enter name: ")
                password = input("Enter Password: ")
                email = input("Enter Email: ")
                address = input("Enter Address: ")
                accType = input("Enter Account Type: ")
                currentuser = User(name, email, address, password, accType)
            

            elif chh=="L" or chh=="l":
                name = input("Enter name: ")
                password = input("Enter Password: ")

                for user in Bank.userAcc:
                    if user.name == name and user.password == password:
                        currentuser = user
                        break

    elif currentuser.name == "admin":
        print(f"\n ______________WELLCOME {currentuser.name} Your Account Number: {currentuser.accNumber}_______________\n")
        print("Choose Options!")
        print("1. Create Account.")
        print("2. Delete User Account.")
        print("3. Show User Account.")
        print("4. Check Total Balance.")
        print("5. Check Total Loan Amount.")
        print("6. Loan Features.")
        print("7. Bankrupt.")
        print("8. Log Out.")
        print()

        op = int(input("Enter Option: "))
        print()

        if op == 1:
            name = input("Enter name: ")
            password = input("Enter Password: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            accType = input("Enter Account Type: ")
            User(name, email, address, password, accType)
        
        elif op == 2:
            name = input("Enter Name: ")
            # accNumber = input("Enter Account Number: ")
            admin.deleteUser(name)
        
        elif op == 3:
            admin.showUser()
        
        elif op==4:
            admin.getBankBalance()

        elif op == 5:
            admin.get_loan()
        elif op==6:
            admin.loan_feature()
        elif op == 7:
            admin.bankrupt()
        else:
            currentuser = None
            # break
    
    else :
        print(f"\n ______________WELLCOME {currentuser.name} Your Account Number: {currentuser.accNumber}_______________\n")
        print("Choose Options!")
        print("1. Deposit.")
        print("2. Withdraw.")
        print("3. Check Balance.")
        print("4. Check History.")
        print("5. Take Loan.")
        print("6. Transfer Amount.")
        print("7. Log Out.")
        print()

        op = int(input("Enter Option: "))
        print()

        if op == 1:
            amount = int(input("Enter Amount: "))
            currentuser.deposit(amount)

        elif op == 2:
            amount = int(input("Enter Amount: "))
            currentuser.withdraw(amount)

        elif op==3:
            currentuser.get_balance()

        elif op == 4:
            currentuser.histories()

        elif op ==5:
            amount = int(input("Enter Loan: "))
            currentuser.take_loan(amount)

        elif op == 6:
            name = input("Enter Transfer name: ")
            amount = int(input("Enter amount: "))
            currentuser.transfer_amount(name, amount)
        else :
            currentuser = None
            # break