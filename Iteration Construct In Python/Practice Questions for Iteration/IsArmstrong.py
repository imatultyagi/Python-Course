# Armstrong number check.
num = int(input("Enter a number: "))
if num < 0:
    print("Please enter a non-negative integer.")
else:
    original_num = num
    sum_of_cubes = 0

    while num > 0:
        digit = num % 10
        sum_of_cubes += digit ** 3
        num //= 10

    if original_num == sum_of_cubes:
        print(f"{original_num} is an Armstrong number.")
    else:
        print(f"{original_num} is not an Armstrong number.")

# Output:
# Enter a number: 153
# 153 is an Armstrong number.
# Enter a number: 123
# 123 is not an Armstrong number.
# Enter a number: -153
# Please enter a non-negative integer.
