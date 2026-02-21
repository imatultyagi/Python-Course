#find largest number taken by user

def find_largest_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
#Input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
#Find the largest numberlargest_num = find_largest_num(num1, num2, num3)
#Output the result
largest_num = find_largest_num(num1, num2, num3)
print("The largest number is: ", largest_num)



# output:Enter the first number: 10
# output:Enter the second number: 20    
# output:Enter the third number: 15
# output:The largest number is:  20.0
