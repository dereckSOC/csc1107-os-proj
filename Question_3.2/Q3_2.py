import numpy as np

# Prompt for user input
user_input = input("Enter a list of numbers separated by space:").split()

# Convert list of strings to a numpy array of integers
arr = np.array(user_input, dtype=int)

#print(arr)

# Function to find largest number in array
def largest(arr):
    max = arr[0] # Initialize max to be the first element

    # Go through the array starting from the second element
    for num in arr[1:]:
        if num > max: # If the number is larger than the existing max value, update max
            max = num
    return max # Return the largest number found

if __name__ == '__main__':
    final = largest(arr) # Call the function to get the largest number
    print(f"{final} is the largest number.") # Display the result