# Problem 59

lst = list(map(int, input("Enter elements separated by space: ").split()))
even = []
odd = []

for num in lst:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)

# Sample Output:
# Enter elements separated by space: 1 2 3 4 5
# Even numbers: [2, 4]
# Odd numbers: [1, 3, 5]