# Check if a number is palindrome

num = int(input("Enter a number: "))
if num < 0:
    print("Please enter a non-negative integer.")
else:
    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    if original_num == reversed_num:
        print(f"{original_num} is a palindrome.")
    else:
        print(f"{original_num} is not a palindrome.")

        
# Output:
# Enter a number: 121
# 121 is a palindrome.
# Enter a number: -121
# Please enter a non-negative integer.
# Enter a number: 10
# 10 is not a palindrome.
