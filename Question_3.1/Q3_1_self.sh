#!/bin/bash

# Since the realm of what is considered a number is not specified, we are just going to assume the most general definition of a number,
# where a number can be positive, negative, an integer, a float.
# So we will not forcible ask the user to input a POSITIVE INTEGER but allow them to input any number of the general definition.

# Function to check if number is prime using trial division
is_prime()
{
    local number=$1

    # Check if number is an integer first
    if ! [[ "$number" =~ ^[-+]?[0-9]*\.?[0]*$ ]]; then
        return 1
    fi

    # Remove leading zeros before decimal
    number=$(echo "$number" | sed -E 's/^([-+]?)(0+)([0-9])/\1\3/')

    # If decimal exists, remove trailing zeros and optional dot
    number=$(echo "$number" | sed -E 's/(\.[0]*$)//')

    # By definition of prime numbers, any integer less than 2 is not prime
    if (( number < 2 )); then
        return 1
    fi
    
    # Get the floor of the square root of the number
    local square_root=$(awk "BEGIN {print int(sqrt($number))}")
    
    # Loop to check if any of the integer from 2 to square root can divide the number
    for (( i=2; i<=square_root; i++ )); do

        # If yes, then number is not prime
        if (( number % i == 0 )); then
            return 1
        fi
    done
    
    # If number cannot be divisible by any of the integer from 2 to square root, then it is a prime number
    return 0 
}

# START OF PROGRAM
# Loop to stay in program unless broken out by user command ctrl C
while true; do
    # Prompt for user input
    read -p "Please key in a number (Ctrl+C to exit): " user_input

    # Error check if user input is a number using regex
    if ! [[ "$user_input" =~ ^[-+]?[0-9]*\.?[0-9]*$ ]]; then
        echo "Input is not a number."
        echo
        continue
    fi
    
    # Print corresponding result to user
    if is_prime "$user_input"; then
        echo "The keyed-in number $user_input is a prime number."
    else
        echo "The keyed-in number $user_input is not a prime number."
    fi
    echo
    # Uncomment to stop after one valid input
    # break
done
