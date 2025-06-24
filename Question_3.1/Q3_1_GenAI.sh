#!/bin/bash

# Infinite loop — will keep running until user interrupts with Ctrl+C
while true; do
    # Prompt user for input
    read -p "Enter a number (or press Ctrl+C to exit): " num

    # Check if input is a valid positive integer
    if ! [[ "$num" =~ ^[0-9]+$ ]]; then
        echo "Invalid input. Please enter a positive integer."
        continue  # Go to next iteration
    fi

    # Numbers less than 2 are not prime
    if [ "$num" -lt 2 ]; then
        echo "The keyed-in number $num is not a prime number"
        continue
    fi

    # Assume the number is prime
    is_prime=1

    # Check divisibility up to square root of num
    for ((i = 2; i * i <= num; i++)); do
        if (( num % i == 0 )); then
            is_prime=0
            break
        fi
    done

    # Print result
    if [ "$is_prime" -eq 1 ]; then
        echo "The keyed-in number $num is a prime number"
    else
        echo "The keyed-in number $num is not a prime number"
    fi

    echo ""  # Print a blank line for readability
done
