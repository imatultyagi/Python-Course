# Problem 79

d = {"b": 2, "a": 1, "c": 3}

sorted_dict = {}

for key in sorted(d.keys()):
    sorted_dict[key] = d[key]

print("Dictionary sorted by keys:", sorted_dict)

# Sample Output:
# Dictionary sorted by keys: {'a': 1, 'b': 2, 'c': 3}