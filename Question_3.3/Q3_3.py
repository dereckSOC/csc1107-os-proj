def question3_3():
    int_list = [1,2,3,4,5,6,7,8,9,10]
    check = False

    try:
        input_num  = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    for i in range(len(int_list)):
        for j in range(i + 1, len(int_list)):
            if int_list[i] + int_list[j] == input_num:
                check = True
                break

    if not check:
        print(f"There are not two numbers in the list summing to the keyed-in number {input_num}.")
    else:
        print(f"There are two numbers in the list summing to the keyed-in number {input_num}.")


question3_3()