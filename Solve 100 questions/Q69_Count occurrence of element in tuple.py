# Problem 69

tpl = tuple(map(int, input("Enter tuple elements: ").split()))
element = int(input("Enter element to count: "))

count = 0
for num in tpl:
    if num == element:
        count += 1

print("Occurrence:", count)

# Sample Output:
# Enter tuple elements: 1 2 2 3 2
# Enter element to count: 2
# Occurrence: 3