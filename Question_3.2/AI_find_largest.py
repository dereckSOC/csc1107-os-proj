#!/usr/bin/env python3

# Define a function to find the largest number in a list
def find_largest(numbers):
    """
    Find and return the largest number in a list of integers.
    
    Args:
        numbers (list): A list of integer numbers
    
    Returns:
        int: The largest number in the list
    """
    # Check if the list is empty
    if not numbers:
        raise ValueError("Error: Empty list provided")
    
    # Validate that all elements are integers
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError(f"Error: '{num}' is not an integer")
    
    # Find the largest number using built-in max function
    largest = max(numbers)
    
    # Print the result
    print(f"{largest} is the largest number")
    
    return largest

# Main block for user input
if __name__ == "__main__":
    try:
        # Ask the user to input space-separated integers
        user_input = input("Enter a list of numbers separated by spaces: ")

        # Convert input string to list of integers
        number_list = list(map(int, user_input.strip().split()))

        # Call the function
        find_largest(number_list)
        
    except ValueError:
        print("Error: Please enter valid integers separated by spaces.")
    except TypeError as e:
        print(e)