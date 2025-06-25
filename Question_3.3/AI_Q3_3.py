def check_sum_pair():
    nums = [2, 4, 5, 7, 9, 11, 13]
    t = int(input("Enter a number: "))
    s = set()
    print(f"There {'are' if any(t - n in s or s.add(n) for n in nums) else 'are not'} two numbers in the list summing to the keyed-in number {t}.")
    
check_sum_pair()