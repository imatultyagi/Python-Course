# Problem 99

text = input("Enter string: ")

print("Substrings:")
for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        print(text[i:j])

# Sample Output:
# Enter string: abc
# Substrings:
# a
# ab
# abc
# b
# bc
# c