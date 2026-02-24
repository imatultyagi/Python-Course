# Problem 47

def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1
    return count

text = input("Enter string: ")
print("Number of vowels =", count_vowels(text))

# Sample Output:
# Enter string: hello
# Number of vowels = 2