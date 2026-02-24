# Problem 96

text = input("Enter string: ")

for ch in text:
    if text.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character found")

# Sample Output:
# Enter string: swiss
# First non-repeating character: w