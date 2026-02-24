# Problem 31

n = int(input("Enter N: "))

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

# Sample Output:
# Enter N: 10
# 2 3 5 7
