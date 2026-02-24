# Problem 1

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)

# Sample Output:
# Enter first number: 5
# Enter second number: 10
# After swapping:
# a = 10
# b = 5