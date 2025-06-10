import numpy as np

user_input = input("Enter a list of numbers separated by space:").split()
arr = np.array(user_input, dtype=int)
n = len(arr)
print(arr)

def largest(arr):
    max = arr[0]

    for num in arr[1:]:
        if num > max:
            max = num
    return max

if __name__ == '__main__':
    final = largest(arr)
    print(f"{final} is the largest number.")