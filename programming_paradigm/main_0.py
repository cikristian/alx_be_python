import sys
from bank_account import BankAccount

def main():
    # Example starting balance of $100
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit:<amount>, withdraw:<amount>, display")
        sys.exit(1)

    # Split command and optional parameter
    parts = sys.argv[1].split(':')
    command = parts[0]
    amount = float(parts[1]) if len(parts) > 1 else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
        account.display_balance()
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
        account.display_balance()
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Use: deposit:<amount>, withdraw:<amount>, or display.")

if __name__ == "__main__":
    main()
