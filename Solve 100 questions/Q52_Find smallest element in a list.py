# Problem 52

lst = list(map(int, input("Enter elements separated by space: ").split()))
smallest = lst[0]

for num in lst:
    if num < smallest:
        smallest = num

print("Smallest element:", smallest)

# Sample Output:
# Enter elements separated by space: 5 2 9 1
# Smallest element: 1