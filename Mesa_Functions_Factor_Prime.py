print("CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM")
print("Created by: Mariann S. Mesa")

def generate_prime(start, end):
    prime = []
    num = max(2, start)

    while num <= end:
        is_prime = True
        i = 2
        while i <= int(num**0.5):
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            prime.append(num)
        num += 1

    return prime
def smallest_factor(n):
    if n < 2:
        return None
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            return i
        i += 1
    return n
def result_prime():
    while True:
        print("Select an option you want to perform: ")
        print("(1) Find the smallest factor of n")
        print("(2) Find prime numbers in range")
        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("Program terminated.")
            return
        elif choice == 1:
            n = int(input("Enter a number: "))
            print(f"The smallest factor of {n} is {smallest_factor(n)}")
        elif choice == 2:
            start = int(input("Enter a number [start]: "))
            end = int(input("Enter a number [end]: "))
            if start < 0 or end <= start:
                print("Invalid input. Please try again.")
                continue
            prime_numbers = generate_prime(start, end)
            print(f"Prime numbers between {start} and {end}: {prime_numbers}")
        else:
            print("Invalid choice. Please choose 1 or 2")

if __name__ == "__main__":
    result_prime()
