int_list=(1 2 3 4 5 6 7 8 9 10)
read -p "Enter a number: " input
check=0

for (( i=0; i<${#int_list[@]}; i++ )); do
    for (( j=i+1; j<${#int_list[@]}; j++ )); do
        sum=$((int_list[i] + int_list[j]))
        if [ "$sum" -eq "$input" ]; then
            check=1
            break 2
        fi
    done
done

if [ "$check" -eq 1 ]; then
    echo "There are two numbers in the list summing to the keyed-in number $input."
else
    echo "There are not two numbers in the list summing to the keyed-in number $input."
fi
