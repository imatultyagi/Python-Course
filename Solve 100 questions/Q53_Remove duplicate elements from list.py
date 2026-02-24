# Problem 53

lst = list(map(int, input("Enter elements separated by space: ").split()))
unique = []

for num in lst:
    if num not in unique:
        unique.append(num)

print("List after removing duplicates:", unique)

# Sample Output:
# Enter elements separated by space: 1 2 2 3 4 4
# List after removing duplicates: [1, 2, 3, 4]