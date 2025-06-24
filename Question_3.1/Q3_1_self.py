# Since the realm of what is considered a number is not specified, we are just going to assume the most general definition of a number,
# where a number can be positive, negative, an integer, a float.
# So we will not forcible ask the user to input a POSITIVE INTEGER but allow them to input any number of the general definition.


# TESTS - 123, 0.123, .123, 00099, 7.0, -1.2, -11.0, -0.234, -000.234, -000.000234, 2.3

import math

# Function to check if number is prime using trial division
def is_prime(number):
    
    # Check if number is an integer first
    if number.is_integer():
        # Convert number to an integer
        integer_number = int(number)
        
        # By definition of prime numbers, any integer less than 2 is not prime
        if integer_number < 2:
            return False
        
        # Get the floor of the square root of the number
        square_root = math.floor(math.sqrt(integer_number))
        
        # Loop to check if any of the integer from 2 to square root can divide the number
        for i in range(2, square_root + 1):
            
            # If yes, then number is not prime
            if integer_number % i == 0:
                return False
        
        # If number cannot be divisible by any of the integer from 2 to square root, then it is a prime number
        return True
        
    else:
        # If number is not an integer, it is not prime
        return False
    

# START OF PROGRAM
# Loop to stay in program unless broken out by user command ctrl C
while(True):
    
    # Prompt for user input
    user_input = input("Please key in a number (Ctrl+C to exit): ")
    try:
        # Convert user input from string to float first
        number = float(user_input)
        
        # Print corresponding result to user
        if is_prime(number):
            print(f"The keyed-in number {user_input} is a prime number.\n")
        else:
            print(f"The keyed-in number {user_input} is not a prime number.\n")
            
        # Uncomment to stop after one valid input
        # break
    except:
        # Error check if user input is a number
        print("Input is not a number.\n")
