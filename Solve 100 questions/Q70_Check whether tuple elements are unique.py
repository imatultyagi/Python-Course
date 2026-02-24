# Problem 70

tpl = tuple(map(int, input("Enter tuple elements: ").split()))
unique = True

for i in range(len(tpl)):
    for j in range(i + 1, len(tpl)):
        if tpl[i] == tpl[j]:
            unique = False
            break

if unique:
    print("All elements are unique")
else:
    print("Elements are not unique")

# Sample Output:
# Enter tuple elements: 1 2 3 4
# All elements are unique