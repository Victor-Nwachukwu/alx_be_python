class BankAccount:
    """
    A simple BankAccount class that represents a banking account with basic operations.
    """
    
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an initial balance.
        
        Args:
            initial_balance (float): The starting balance for the account. Defaults to 0.
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): The amount to deposit
            
        Returns:
            bool: True if deposit was successful
        """
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            print("Error: Deposit amount must be positive.")
            return False
    
    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds are available.
        
        Args:
            amount (float): The amount to withdraw
            
        Returns:
            bool: True if withdrawal was successful, False if insufficient funds
        """
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        elif amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            print("Error: Insufficient funds for withdrawal.")
            return False
    
    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")