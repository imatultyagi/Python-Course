# Problem 66

tpl = tuple(map(int, input("Enter tuple elements: ").split()))
maximum = tpl[0]

for num in tpl:
    if num > maximum:
        maximum = num

print("Maximum value:", maximum)

# Sample Output:
# Enter tuple elements: 5 2 9 1
# Maximum value: 9