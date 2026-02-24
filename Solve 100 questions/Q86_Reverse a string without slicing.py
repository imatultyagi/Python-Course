# Problem 86

text = input("Enter string: ")
reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string:", reverse)

# Sample Output:
# Enter string: hello
# Reversed string: olleh