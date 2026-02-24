# Problem 95

text = input("Enter string: ")
result = ""

for ch in text:
    if ch not in result:
        result += ch

print("String after removing duplicates:", result)

# Sample Output:
# Enter string: programming
# String after removing duplicates: progamin