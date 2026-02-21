#average of number taken by users 
def calculate_average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    return average
#Input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
#Calculate average
average = calculate_average(num1, num2, num3)
#Output the result
print("The average of the three numbers is: ", average)



# output:Enter the first number: 10
# output:Enter the second number: 20
# output:Enter the third number: 30
# output:The average of the three numbers is:  20.0

