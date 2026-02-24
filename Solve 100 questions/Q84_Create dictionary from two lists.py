# Problem 84

keys = input("Enter keys separated by space: ").split()
values = list(map(int, input("Enter values separated by space: ").split()))

d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

print("Created dictionary:", d)

# Sample Output:
# Enter keys separated by space: a b c
# Enter values separated by space: 1 2 3
# Created dictionary: {'a': 1, 'b': 2, 'c': 3}