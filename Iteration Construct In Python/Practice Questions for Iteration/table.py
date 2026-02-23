# Print multiplication table of a number (input from user)

num = int(input("Enter a number: "))
if num < 1:
    print("Please enter a positive integer.")
else:
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

#Output:
# Enter a number: 5
# 5 x 1 = 5
# 5 x 2 = 10    
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

