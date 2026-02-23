#Inventory Management

def manage_inventory(stock_quantities):
    # Remove items with 0 stock
    valid_stock = [stock for stock in stock_quantities if stock > 0]

    # Add restock to items below 10
    updated_stock = []
    for stock in valid_stock:
        if stock < 10:
            stock += 50  # Add restock
        updated_stock.append(stock)

    # Find total inventory count
    total_inventory = sum(updated_stock)

    return total_inventory
# Example usage
stock_list = [0, 5, 15, 8, 20]  # Contains items with 0 stock and items below 10
total_count = manage_inventory(stock_list)
print(f"Total inventory count: {total_count}")
#output: Total inventory count: 98
