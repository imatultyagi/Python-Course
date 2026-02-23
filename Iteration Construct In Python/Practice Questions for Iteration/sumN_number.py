# Find sum of first N natural numbers.
n = int(input("Enter a number: "))
if n < 1:
    print("Please enter a positive integer.")
else:
    sum_natural = n * (n + 1) // 2
    print(f"The sum of the first {n} natural numbers is: {sum_natural}")
    
# Output:
# Enter a number: 5
# The sum of the first 5 natural numbers is: 15
