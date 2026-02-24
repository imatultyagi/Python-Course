# Problem 54

lst = list(map(int, input("Enter elements separated by space: ").split()))

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("Sorted list:", lst)

# Sample Output:
# Enter elements separated by space: 4 2 1 3
# Sorted list: [1, 2, 3, 4]