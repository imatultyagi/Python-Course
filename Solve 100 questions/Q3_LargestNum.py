# Problem 3

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c

print("Largest number is:", largest)

# Sample Output:
# Enter first number: 10
# Enter second number: 25
# Enter third number: 15
# Largest number is: 25