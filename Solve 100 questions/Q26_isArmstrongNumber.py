# Problem 26

num = int(input("Enter number: "))
temp = num
sum_digits = 0
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_digits += digit ** digits
    temp //= 10

if sum_digits == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

# Sample Output:
# Enter number: 153
# Armstrong Number