# Find largest digit in a number

num = int(input("Enter a number: "))
if num < 0:
    print("Please enter a non-negative integer.")
else:
    largest_digit = 0
    while num > 0:
        digit = num % 10
        if digit > largest_digit:
            largest_digit = digit
        num //= 10

    print(f"The largest digit in the number is: {largest_digit}")

    
    # Output:
    # Enter a number: 12345
    # The largest digit in the number is: 5
    # Enter a number: 9876543210
    # The largest digit in the number is: 9
    # Enter a number: -123
    # Please enter a non-negative integer.
