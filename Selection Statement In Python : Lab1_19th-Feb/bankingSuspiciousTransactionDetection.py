#program to flag transactions for manual verification based on certain criteria 
amount = float(input("Enter the transaction amount: "))
 #Ammount Validation
if amount <=0:
        print("Invalid amount. Please enter a positive value.")
        exit(0) 
account_age = int(input("Enter the account age in months: "))
#Account age validation
if account_age <= 0 or account_age > 12:
        print("Invalid account age. Please enter a value between 1 and 12 months.")
        exit(0)
#transaction type validation 
is_international = input("Is the transaction international? (yes/no): ").lower()
if amount > 200000 and account_age < 6 and is_international == "yes":
    print("The transaction should be flagged for manual verification.")
