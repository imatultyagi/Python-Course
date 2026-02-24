# Problem 64

lst = list(map(int, input("Enter elements: ").split()))

for i in range(len(lst)):
    if lst[i] < 0:
        lst[i] = 0

print("Updated list:", lst)

# Sample Output:
# Enter elements: -1 5 -3 7
# Updated list: [0, 5, 0, 7]