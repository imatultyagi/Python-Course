# Problem 57

lst = list(map(int, input("Enter elements separated by space: ").split()))
reverse = []

for i in range(len(lst)-1, -1, -1):
    reverse.append(lst[i])

print("Reversed list:", reverse)

# Sample Output:
# Enter elements separated by space: 1 2 3 4
# Reversed list: [4, 3, 2, 1]