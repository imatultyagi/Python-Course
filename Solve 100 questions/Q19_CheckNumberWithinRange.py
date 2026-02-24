# Problem 19

num = int(input("Enter number: "))
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))

if low <= num <= high:
    print("Number is within range")
else:
    print("Number is outside range")

# Sample Output:
# Enter number: 5
# Enter lower limit: 1
# Enter upper limit: 10
# Number is within range