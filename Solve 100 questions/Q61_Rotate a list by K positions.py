# Problem 61

lst = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter rotation value K: "))

k = k % len(lst)
rotated = lst[k:] + lst[:k]

print("Rotated list:", rotated)

# Sample Output:
# Enter elements: 1 2 3 4 5
# Enter rotation value K: 2
# Rotated list: [3, 4, 5, 1, 2]