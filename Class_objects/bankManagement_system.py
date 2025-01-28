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
        if len(account_number) != 14 or not account_number.isdigit():
            print("Account number must be 14 digits long and numeric.")
            return
        if not holder_name.isalpha() or not holder_name.strip():
            print("Account holder name should contain only alphabetic characters..")
            return
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[account_number] = {"holder_name": holder_name, "balance": 0}
            print(f"Account {account_number} for {holder_name} created successfully.")


    def deposit(self, account_number, amount):
        """Deposit money into an account."""
        try:
            if account_number in self.accounts:
                if not self.is_numeric(amount):
                    print("Amount must be a numeric value.")
                    return
                self.accounts[account_number]["balance"] += amount
                print(f"Deposited {amount} to account {account_number}.")
            else:
                print("Account number not found.")
        except Exception as e:
            print(f"Error during deposit: {e}")


    def withdraw(self, account_number, amount):
        """Withdraw money from an account but prevent negative balance."""
        try:
            if account_number in self.accounts:
                if not self.is_numeric(amount):
                    print("Amount must be a numeric value.")
                    return
                if self.accounts[account_number]["balance"] >= amount:
                    self.accounts[account_number]["balance"] -= amount
                    print(f"Withdrawn {amount} from account {account_number}.")
                else:
                    print(f"Insufficient balance! Your current balance is {self.accounts[account_number]['balance']}. Withdrawal of {amount} is not possible.")
            else:
                print("Account number not found.")
        except Exception as e:
            print(f"Error during withdrawal: {e}")


    def available_balance(self, account_number):
        """Display the current balance of a specified account."""
        try:
            if account_number in self.accounts:
                balance = self.accounts[account_number]["balance"]
                holder_name = self.accounts[account_number]["holder_name"]
                print(f"Account Holder: {holder_name}, Balance: {balance}")
            else:
                print("Account number not found.")
        except Exception as e:
            print(f"Error fetching balance: {e}")


    def is_numeric(self, value):
        """Check if the value is numeric."""
        return isinstance(value, (int, float)) or (isinstance(value, str) and value.replace('.', '', 1).isdigit())


class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest_rate = 0.05


    def calculate_interest(self, account_number):
        """Calculate interest for a given account."""
        try:
            if account_number in self.accounts:
                balance = self.accounts[account_number]["balance"]
                interest = balance * self.interest_rate
                print(f"Interest for account {account_number}: {interest}")
                return interest
            else:
                print("Account number not found.")
                return 0
        except Exception as e:
            print(f"Error calculating interest: {e}")
            return 0


    def apply_interest(self, account_number):
        """Apply interest to the balance of the given account."""
        try:
            if account_number in self.accounts:
                interest = self.calculate_interest(account_number)
                self.accounts[account_number]["balance"] += interest
                print(f"Interest applied to account {account_number}. New balance: {self.accounts[account_number]['balance']}")
            else:
                print("Account number not found.")
        except Exception as e:
            print(f"Error applying interest: {e}")


class CurrentAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.overdraft_limit = 1000


    def withdraw(self, account_number, amount):
        """Withdraw money, allowing overdraft within the limit."""
        try:
            if account_number in self.accounts:
                if not self.is_numeric(amount):
                    print("Amount must be a numeric value.")
                    return
                balance = self.accounts[account_number]["balance"]
                if balance + self.overdraft_limit >= amount:
                    self.accounts[account_number]["balance"] -= amount
                    print(f"Withdrawn {amount} from account {account_number}.")
                else:
                    print("Withdrawal exceeds overdraft limit.")
            else:
                print("Account number not found.")
        except Exception as e:
            print(f"Error during withdrawal: {e}")




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


        try:
            if choice == "1":
                account_number = input("Enter Savings Account number (14 digits): ")
                holder_name = input("Enter Account Holder's Name: ")
                savings.create_account(account_number, holder_name)  


            elif choice == "2":
                account_number = input("Enter Current Account number (14 digits): ")
                holder_name = input("Enter Account Holder's Name: ")
                current.create_account(account_number, holder_name)  


            elif choice == "3":
                account_number = input("Enter Account Number for Deposit: ")
                amount = input("Enter Amount to Deposit: ")
                if not amount.isdigit():
                    print("Amount must be a numeric value.")
                    continue
                amount = float(amount)
                if account_number in savings.accounts:  
                    savings.deposit(account_number, amount)
                elif account_number in current.accounts:  
                    current.deposit(account_number, amount)
                else:
                    print("Account number not found.")


            elif choice == "4":
                account_number = input("Enter Account Number for Withdrawal: ")
                amount = input("Enter Amount to Withdraw: ")
                if not amount.isdigit():
                    print("Amount must be a numeric value.")
                    continue
                amount = float(amount)
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
                amount = input("Enter Amount to Withdraw (Including Overdraft): ")
                if not amount.isdigit():
                    print("Amount must be a numeric value.")
                    continue
                amount = float(amount)
                if account_number in current.accounts:  
                    current.withdraw(account_number, amount)  
                else:
                    print("Account number not found in Current Accounts.")


            elif choice == "9":
                print("Thank you for using the bank system. Goodbye!")
                break


            else:
                print("Invalid choice. Please try again.")


        except Exception as e:
            print(f"An error occurred: {e}")


main()

