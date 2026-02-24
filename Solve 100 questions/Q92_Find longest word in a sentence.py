# Problem 92

sentence = input("Enter sentence: ")
words = sentence.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

# Sample Output:
# Enter sentence: Python programming is powerful
# Longest word: programming