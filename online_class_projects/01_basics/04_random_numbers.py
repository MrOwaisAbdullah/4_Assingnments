import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    print("\n\033[01m\033[03mHere are 10 random numbers between 1 and 100:\033[0m\n")
    for number in numbers:
        print(number, end=" ")
    print("\n")

if __name__ == '__main__':
    main()