# Problem 78

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {}

for key in dict1:
    merged[key] = dict1[key]

for key in dict2:
    merged[key] = dict2[key]

print("Merged dictionary:", merged)

# Sample Output:
# Merged dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}