# Problem 67

tpl = tuple(map(int, input("Enter tuple elements: ").split()))
minimum = tpl[0]

for num in tpl:
    if num < minimum:
        minimum = num

print("Minimum value:", minimum)

# Sample Output:
# Enter tuple elements: 5 2 9 1
# Minimum value: 1