# Problem 87

text = input("Enter string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Sample Output:
# Enter string: madam
# Palindrome