#Program to cakculate simple interest
#Formula for simple interest is SI = (P * R * T) / 100
#Where P is the principal amount, R is the rate of interest and T is the time in years
#Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest
#Input from user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
#Calculate simple interest
simple_interest = calculate_simple_interest(principal, rate, time)
#Output the result
print("The simple interest is: ", simple_interest)


# output:Enter the principal amount: 1000
# output:Enter the rate of interest: 5
# output:Enter the time in years: 2
# output:The simple interest is:  100.0

