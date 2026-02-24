# Problem 58

lst1 = list(map(int, input("Enter first list: ").split()))
lst2 = list(map(int, input("Enter second list: ").split()))

merged = lst1 + lst2
unique = []

for num in merged:
    if num not in unique:
        unique.append(num)

print("Merged list without duplicates:", unique)

# Sample Output:
# Enter first list: 1 2 3
# Enter second list: 2 3 4
# Merged list without duplicates: [1, 2, 3, 4]