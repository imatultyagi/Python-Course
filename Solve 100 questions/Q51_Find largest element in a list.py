# Problem 51

lst = list(map(int, input("Enter elements separated by space: ").split()))
largest = lst[0]

for num in lst:
    if num > largest:
        largest = num

print("Largest element:", largest)

# Sample Output:
# Enter elements separated by space: 5 2 9 1
# Largest element: 9