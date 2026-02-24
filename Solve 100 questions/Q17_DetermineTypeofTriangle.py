# Problem 17

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# Sample Output:
# Enter side 1: 5
# Enter side 2: 5
# Enter side 3: 5
# Equilateral Triangle