# This program simulates an ATM withdrawal process, checking for sufficient account balance, daily withdrawal limits, and ATM cash availability before allowing a withdrawal.
 
account_balance = float(input("Enter your account balance: "))
# Account balance validation
if account_balance < 0:
    print("Invalid account balance. Please enter a positive value.")
    exit(0)
withdrawal_amount = float(input("Enter the withdrawal amount: "))
# Withdrawal amount validation
if withdrawal_amount < 0:
    print("Invalid withdrawal amount. Please enter a positive value.")
    exit(0)
daily_withdrawal_limit = 50000
atm_cash_available = 100000  # Example cash availability in the ATM
if withdrawal_amount > account_balance:
    print("Withdrawal failed: Insufficient account balance.")
elif withdrawal_amount > daily_withdrawal_limit:
    print("Withdrawal failed: Exceeds daily withdrawal limit of ₹50,000.")
elif withdrawal_amount > atm_cash_available:
    print("Withdrawal failed: ATM does not have sufficient cash available.")
else:
    print("Withdrawal successful. Please collect your cash.")
