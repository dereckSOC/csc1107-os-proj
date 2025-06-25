#!/bin/bash

numbers=(2 4 5 7 9 11 13)
read -p "Enter a number: " target

for ((i=0; i<${#numbers[@]}; i++)); do
  for ((j=i+1; j<${#numbers[@]}; j++)); do
    ((numbers[i] + numbers[j] == target)) && {
      echo "There are two numbers in the list summing to the keyed-in number $target."
      exit 0
    }
  done
done

echo "There are not two numbers in the list summing to the keyed-in number $target."
