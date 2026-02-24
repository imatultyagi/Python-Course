# Problem 35

text = input("Enter string: ")
count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)

# Sample Output:
# Enter string: hello
# Number of vowels: 2