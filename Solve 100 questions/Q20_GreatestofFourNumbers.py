# Problem 20

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

greatest = a

if b > greatest:
    greatest = b
if c > greatest:
    greatest = c
if d > greatest:
    greatest = d

print("Greatest number is:", greatest)

# Sample Output:
# Enter first number: 10
# Enter second number: 45
# Enter third number: 23
# Enter fourth number: 30
# Greatest number is: 45