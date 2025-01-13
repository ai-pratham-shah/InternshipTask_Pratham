''' Create a Banking system using class, Methods, and Inheritance.
Explanation:
Base Class (BankAccount):

Contains attributes for account number, holder, and balance.
Includes methods for deposit, withdrawal, and displaying balance.
Derived Classes:

SavingsAccount: Adds interest rate, interest calculation, and application methods.
CurrentAccount: Adds overdraft limit and modifies the withdrawal method to allow overdrafts within the limit.
Example Usage:

Demonstrates how to create and interact with SavingsAccount and CurrentAccount objects. '''



class BankAccount:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, holder_name):
        """Create a new account with a holder's name."""
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[account_number] = {"holder_name": holder_name, "balance": 0}
            print(f"Account {account_number} for {holder_name} created successfully.")

    def deposit(self, account_number, amount):
        """Deposit money into an account."""
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            print(f"Deposited {amount} to account {account_number}.")
        else:
            print("Account number not found.")

    def withdraw(self, account_number, amount):
        """Withdraw money from an account."""
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                print(f"Withdrawn {amount} from account {account_number}.")
            else:
                print("Insufficient balance.")
        else:
            print("Account number not found.")

    def available_balance(self, account_number):
        """Display the current balance of a specified account."""
        if account_number in self.accounts:
            balance = self.accounts[account_number]["balance"]
            holder_name = self.accounts[account_number]["holder_name"]
            print(f"Account Holder: {holder_name}, Balance: {balance}")
        else:
            print("Account number not found.")
class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest_rate = 0.05  # Example interest rate: 5%

    def calculate_interest(self, account_number):
        """Calculate interest for a given account."""
        if account_number in self.accounts:
            balance = self.accounts[account_number]["balance"]
            interest = balance * self.interest_rate
            print(f"Interest for account {account_number}: {interest}")
            return interest
        else:
            print("Account number not found.")
            return 0

    def apply_interest(self, account_number):
        """Apply interest to the balance of the given account."""
        interest = self.calculate_interest(account_number)
        self.accounts[account_number]["balance"] += interest
        print(f"Interest applied to account {account_number}. New balance: {self.accounts[account_number]['balance']}")


class CurrentAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.overdraft_limit = 1000 

    def withdraw(self, account_number, amount):
        """Withdraw money, allowing overdraft within the limit."""
        if account_number in self.accounts:
            balance = self.accounts[account_number]["balance"]
            if balance + self.overdraft_limit >= amount:
                self.accounts[account_number]["balance"] -= amount
                print(f"Withdrawn {amount} from account {account_number}.")
            else:
                print("Withdrawal exceeds overdraft limit.")
        else:
            print("Account number not found.")
# Menu-driven interaction
def main():
    savings = SavingsAccount()   
    current = CurrentAccount()   

    while True:
        print("\n!!!!!! Welcome to the Bank !!!!!!")
        print("1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit Amount")
        print("4. Withdraw Amount")
        print("5. Check Balance")
        print("6. Calculate Interest (Savings Account Only)")
        print("7. Apply Interest (Savings Account Only)")
        print("8. Withdraw with Overdraft (Current Account Only)")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            account_number = input("Enter Savings Account number: ")
            holder_name = input("Enter Account Holder's Name: ")
            savings.create_account(account_number, holder_name)  

        elif choice == "2":
            account_number = input("Enter Current Account number: ")
            holder_name = input("Enter Account Holder's Name: ")
            current.create_account(account_number, holder_name)  

        elif choice == "3":
            account_number = input("Enter Account Number for Deposit: ")
            amount = float(input("Enter Amount to Deposit: "))
            if account_number in savings.accounts:   
                savings.deposit(account_number, amount)
            elif account_number in current.accounts:  
                current.deposit(account_number, amount)
            else:
                print("Account number not found.")

        elif choice == "4":
            account_number = input("Enter Account Number for Withdrawal: ")
            amount = float(input("Enter Amount to Withdraw: "))
            if account_number in savings.accounts:   
                savings.withdraw(account_number, amount)
            elif account_number in current.accounts:  
                current.withdraw(account_number, amount)
            else:
                print("Account number not found.")
        
        elif choice == "5":
            account_number = input("Enter Account Number to Check Balance: ")
            if account_number in savings.accounts:   
                savings.available_balance(account_number)
            elif account_number in current.accounts:  
                current.available_balance(account_number)
            else:
                print("Account number not found.")
        
        elif choice == "6":
            account_number = input("Enter Savings Account Number to Calculate Interest: ")
            savings.calculate_interest(account_number)

        elif choice == "7":
            account_number = input("Enter Savings Account Number to Apply Interest: ")
            savings.apply_interest(account_number)

        elif choice == "8":
            account_number = input("Enter Current Account Number for Withdrawal with Overdraft: ")
            amount = float(input("Enter Amount to Withdraw (Including Overdraft): "))
            if account_number in current.accounts:  
                current.withdraw(account_number, amount)  
            else:
                print("Account number not found.")

        elif choice == "9":
            print("Thank you for using the bank system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()
