#!/bin/bash

# Function to find the largest number in a list
find_largest() {
    # Check if any arguments were provided
    if [ $# -eq 0 ]; then
        echo "Error: No numbers provided"
        echo "Usage: $0 number1 number2 number3 ..."
        exit 1
    fi
    
    # Initialize largest with the first argument
    largest=$1
    
    # Loop through all arguments
    for num in "$@"; do
        # Check if the argument is a valid integer
        if ! [[ "$num" =~ ^-?[0-9]+$ ]]; then
            echo "Error: '$num' is not a valid integer"
            exit 1
        fi
        
        # Compare and update largest if current number is bigger
        if [ "$num" -gt "$largest" ]; then
            largest=$num
        fi
    done
    
    # Print the result
    echo "$largest is the largest number"
}

# Example usage with predefined list (uncomment to use)
# numbers=(45 23 78 12 99 34 67)
# find_largest "${numbers[@]}"

# Call function with command line arguments
find_largest "$@"