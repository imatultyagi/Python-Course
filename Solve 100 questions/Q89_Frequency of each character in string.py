# Problem 89

text = input("Enter string: ")
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character frequency:", freq)

# Sample Output:
# Enter string: apple
# Character frequency: {'a': 1, 'p': 2, 'l': 1, 'e': 1}