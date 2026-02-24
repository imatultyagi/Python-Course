# Problem 46

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)

# Sample Output:
# Enter number of terms: 5
# 0 1 1 2 3