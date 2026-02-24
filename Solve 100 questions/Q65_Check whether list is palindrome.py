# Problem 65

lst = list(map(int, input("Enter elements: ").split()))

if lst == lst[::-1]:
    print("Palindrome List")
else:
    print("Not a Palindrome List")

# Sample Output:
# Enter elements: 1 2 3 2 1
# Palindrome List