# Problem 81

d = {}
n = int(input("Enter number of items: "))

for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value
    

max_key = max(d, key=d.get) # type: ignore

print("Key with maximum value:", max_key)
print("Maximum value:", d[max_key])

# Sample Output:
# Enter number of items: 2
# Enter key: A
# Enter value: 10
# Enter key: B
# Enter value: 20
# Key with maximum value: B
# Maximum value: 20