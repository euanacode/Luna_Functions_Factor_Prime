# For finding the smallest factor and prime numbers in range

def find_smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than 2")
        return

    for i in range(2, n + 1):
        if n % i == 0:
            print(f"The smallest factor other than 1 for {n} is {i}.")
            break


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def display_primes(start, end):
    if start < 1:
        print("Please enter a non-negative number.")
        return

    if end < start:
        print(f"Enter a number greater than {start}.")
        return

    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")


if __name__ == "__main__":
    while True:
        print("Menu: ")
        print(" ")
        print("Press 1 to Find The Smallest Factor Of A Number.")
        print("Press 2 to Display Prime Numbers In A Range.")
        print("Press 0 to Exit")
        print(" ")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Program terminated.")
            break
        elif choice == 1:
            try:
                factor_input = int(input("Enter an number >= 2: "))
                find_smallest_factor(factor_input)
            except ValueError:
                print("Invalid input. Enter a valid number.")
        elif choice == 2:
            while True:
                start = int(input("Enter a number (start): "))

                if start < 0:
                    print("Please enter a non-negative number.")
                    continue

                if start == 0:
                    print("Program terminated.")
                    break

                end = int(input("Enter a number (end): "))

                if end < start:
                    print(f"Enter a number greater than {start}.")
                else:
                    display_primes(start, end)
                    print("\n")
        else:
            print("Invalid Choice. Please enter 0, 1, or 2 to continue.")
