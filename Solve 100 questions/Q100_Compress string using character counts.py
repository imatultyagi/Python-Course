# Problem 100

text = input("Enter string: ")
compressed = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        compressed += text[i - 1] + str(count)
        count = 1

compressed += text[-1] + str(count)

print("Compressed string:", compressed)

# Sample Output:
# Enter string: aaabbc
# Compressed string: a3b2c1