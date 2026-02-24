# Problem 82

d = {"a": 1, "b": 2, "c": 3}

key = input("Enter key to remove: ")

if key in d:
    del d[key]
    print("Key removed.")
else:
    print("Key not found.")

print("Updated dictionary:", d)

# Sample Output:
# Enter key to remove: b
# Key removed.
# Updated dictionary: {'a': 1, 'c': 3}