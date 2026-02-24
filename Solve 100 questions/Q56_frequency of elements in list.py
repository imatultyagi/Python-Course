# Problem 56

lst = list(map(int, input("Enter elements separated by space: ").split()))
freq = {}

for num in lst:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency:", freq)

# Sample Output:
# Enter elements separated by space: 1 2 2 3 1 1
# Frequency: {1: 3, 2: 2, 3: 1}