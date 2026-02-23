#Bank Transaction Analyzer
def analyze_transactions(transactions):
    # Calculate total balance
    total_balance = sum(transactions)
    # Find largest withdrawal
    largest_withdrawal = min(transactions)  # Since withdrawals are negative, the minimum value is the largest withdrawal
    # Count number of deposits greater than ₹10,000
    large_deposits_count = sum(1 for transaction in transactions if transaction > 10000)
    return {
        "total_balance": total_balance,
        "largest_withdrawal": largest_withdrawal,
        "large_deposits_count": large_deposits_count
    }
# Example usage
transaction_list = [5000, -2000, 15000, -500, 3000, -10000, 20000]  # Contains deposits and withdrawals
result = analyze_transactions(transaction_list)
print(result)
#output: {'total_balance': 33000, 'largest_withdrawal': -10000, 'large_deposits_count': 2}
