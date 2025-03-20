import math

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def main():
    print("Pythagorean Theorem\n")
    while True:
        side_a = input("\033[1m\033[3mEnter the length of side a:\033[0m\n")
        if is_float(side_a):
            break
        else:
            print("\033[91m\033[1m\033[4mError:\033[0m\033[91m Please enter a valid number.\033[0m\n")

    while True:
        side_b = input("\033[1m\033[3mEnter the length of side b:\033[0m\n")
        if is_float(side_b):
            break
        else:
            print("\033[91m\033[1m\033[4mError:\033[0m\033[91m Please enter a valid number.\033[0m\n")

    side_c: float = math.sqrt(float(side_a) ** 2 + float(side_b) ** 2)

    print("\n\033[1m\033[3mResults:\033[0m\n")
    print("a^2 + b^2 = c^2...")
    print("a = " + str(side_a) + " units")
    print("b = " + str(side_b) + " units\n")
    print(f"The length of the hypotenuse is {side_c} units!\n")

if __name__ == "__main__":
    main()