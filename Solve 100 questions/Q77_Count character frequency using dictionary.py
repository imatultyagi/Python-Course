# Problem 77

text = input("Enter string: ")
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character frequency:", freq)

# Sample Output:
# Enter string: hello
# Character frequency: {'h': 1, 'e': 1, 'l': 2, 'o': 1}