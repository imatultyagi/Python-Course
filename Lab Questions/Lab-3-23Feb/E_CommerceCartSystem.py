#E-Commerce Cart System 

def calculate_final_amount(prices):
    # Remove duplicate items
    unique_prices = list(set(prices))

    # Calculate total
    total = sum(unique_prices)

    # Apply discount if total > ₹5000
    if total > 5000:
        total *= 0.9  # Apply 10% discount

    # Add GST 18%
    final_amount = total * 1.18

    return final_amount

# Example usage
cart_prices = [1000, 2000, 3000, 1000, 2000]  # Duplicate items
final_amount = calculate_final_amount(cart_prices)
print(f"Final payable amount: ₹{final_amount:.2f}")

#output: Final payable amount: ₹7080.00
