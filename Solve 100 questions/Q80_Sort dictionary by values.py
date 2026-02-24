# Problem 80

d = {"a": 3, "b": 1, "c": 2}

sorted_items = sorted(d.items(), key=lambda x: x[1])
sorted_dict = {}

for key, value in sorted_items:
    sorted_dict[key] = value

print("Dictionary sorted by values:", sorted_dict)

# Sample Output:
# Dictionary sorted by values: {'b': 1, 'c': 2, 'a': 3}