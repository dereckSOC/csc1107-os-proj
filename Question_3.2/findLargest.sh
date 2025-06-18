#!/bin/bash

# Prompt for user input
printf "Enter a list of numbers, with spaces: "
read -a ARRAY

# Initialize MAX with the first element
MAX=${ARRAY[0]}

# Iterate through the elements of the array
for i in ${!ARRAY[@]}; do
    # Compare current element with MAX
    if [ ${ARRAY[$i]} -gt $MAX ]; then 
        MAX=${ARRAY[$i]} # Update MAX if current element is larger than MAX
    fi
done

# Print the result
echo "$MAX is the largest number."
