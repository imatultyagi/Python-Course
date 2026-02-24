# Problem 93

text = input("Enter string: ")
result = ""

for ch in text:
    if ch.lower() in "aeiou":
        result += "*"
    else:
        result += ch

print("Modified string:", result)

# Sample Output:
# Enter string: hello
# Modified string: h*ll*