def is_prime_number():
    # Prompt the user to enter a number
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Invalid input. Please enter an integer.")
        return

    # Check if the number is less than or equal to 1 (not prime)
    if num <= 1:
        print(f"The keyed-in number {num} is not a prime number.")
        return

    # Check for factors from 2 up to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            # If divisible by any number in the range, it's not prime
            print(f"The keyed-in number {num} is not a prime number.")
            return

    # If no divisors found, the number is prime
    print(f"The keyed-in number {num} is a prime number.")

# Call the function to run it
is_prime_number()
