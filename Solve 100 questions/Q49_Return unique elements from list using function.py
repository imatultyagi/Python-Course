# Problem 49

def unique_elements(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

lst = list(map(int, input("Enter list elements separated by space: ").split()))
print("Unique elements:", unique_elements(lst))

# Sample Output:
# Enter list elements separated by space: 1 2 2 3 4 4
# Unique elements: [1, 2, 3, 4]