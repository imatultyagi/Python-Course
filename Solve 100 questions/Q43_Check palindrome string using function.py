# Problem 43

def is_palindrome(text):
    return text == text[::-1]

text = input("Enter string: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")

# Sample Output:
# Enter string: madam
# Palindrome