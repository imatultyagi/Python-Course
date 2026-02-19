# This program evaluates a loan application based on the applicant's credit score, monthly income, and existing loan amount.
 
credit_score = int(input("Enter your credit score: "))
#Credit score validation
if credit_score < 0 or credit_score > 850:
    print("Invalid credit score. Please enter a value between 0 and 850.")
    exit(0)
monthly_income = float(input("Enter your monthly income: "))
#Monthly income validation
if monthly_income < 0:
    print("Invalid monthly income. Please enter a positive value.")
    exit(0)
existing_loan_amount = float(input("Enter your existing loan amount: "))
#Existing loan amount validation
if existing_loan_amount < 0:
    print("Invalid existing loan amount. Please enter a positive value.")
    exit(0)
if credit_score < 600:
    print("Loan application rejected due to low credit score.")
elif credit_score >= 600 and credit_score < 750:
    if monthly_income < 30000 and existing_loan_amount > 500000:
        print("Loan application rejected due to insufficient income and high existing loan amount.")
    else:
        print("Loan application approved after further checks.")
