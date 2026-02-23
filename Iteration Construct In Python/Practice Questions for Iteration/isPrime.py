# Check if a number is prime.
num = int(input("Enter a number: "))
if num < 2:
    print("Please enter an integer greater than or equal to 2.")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

        
# Output:
# Enter a number: 7
# 7 is a prime number.
# Enter a number: 10
# 10 is not a prime number.