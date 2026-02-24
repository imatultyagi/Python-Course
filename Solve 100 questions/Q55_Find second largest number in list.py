# Problem 55

lst = list(map(int, input("Enter elements separated by space: ").split()))
largest = second = float('-inf')

for num in lst:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)

# Sample Output:
# Enter elements separated by space: 5 8 3 9 2
# Second largest: 8