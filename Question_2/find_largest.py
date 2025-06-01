#!/usr/bin/env python3

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

def find_largest_manual(numbers):
    """
    Alternative implementation without using built-in max() function.
    
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
    
    # Initialize largest with the first element
    largest = numbers[0]
    
    # Loop through the rest of the numbers
    for num in numbers[1:]:
        if num > largest:
            largest = num
    
    # Print the result
    print(f"{largest} is the largest number")
    
    return largest

# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_lists = [
        [45, 23, 78, 12, 99, 34, 67],
        [1, 2, 3, 4, 5],
        [-10, -5, -20, -1],
        [42],
        [100, 25, 75, 50, 125, 10]
    ]
    
    print("Testing find_largest function:")
    print("-" * 40)
    
    for i, test_list in enumerate(test_lists, 1):
        print(f"Test {i}: {test_list}")
        try:
            result = find_largest(test_list)
            print(f"Returned value: {result}")
        except (ValueError, TypeError) as e:
            print(e)
        print()
    
    print("Testing find_largest_manual function:")
    print("-" * 40)
    
    # Test the manual implementation with one example
    test_list = [45, 23, 78, 12, 99, 34, 67]
    print(f"Test: {test_list}")
    result = find_largest_manual(test_list)
    print(f"Returned value: {result}")