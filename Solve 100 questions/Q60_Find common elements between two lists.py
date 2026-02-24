# Problem 60

lst1 = list(map(int, input("Enter first list: ").split()))
lst2 = list(map(int, input("Enter second list: ").split()))

common = []

for num in lst1:
    if num in lst2 and num not in common:
        common.append(num)

print("Common elements:", common)

# Sample Output:
# Enter first list: 1 2 3 4
# Enter second list: 3 4 5 6
# Common elements: [3, 4]