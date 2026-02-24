# Problem 14

ch = input("Enter a character: ")

if ch.isdigit():
    print("Digit")
elif ch.isalpha():
    print("Alphabet")
else:
    print("Special Character")

# Sample Output:
# Enter a character: 5
# Digit