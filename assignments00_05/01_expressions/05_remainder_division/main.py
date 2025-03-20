def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def main():
    while True:
        num1 = input("\033[1m\033[3mPlease enter an integer to be divided: \n\033[0m")
        if is_float(num1):
            break
        else:
            print("\033[91m\033[1m\033[4mError:\033[0m\033[91m Please enter a valid number.\033[0m\n")
    while True:
        num2 = input("\033[1m\033[3mPlease enter an integer to divide by: \n\033[0m")
        if is_float(num2):
            break
        else:
            print("\033[91m\033[1m\033[4mError:\033[0m\033[91m Please enter a valid number.\033[0m\n")

    divided = float(num1) / float(num2)
    remainder = float(num1) % float(num2)

    print("\n\033[1m\033[3mResults:\033[0m\n")
    print(f"{num1} divided by {num2} is {divided} with a remainder of {remainder}.\n")
    
if __name__ == "__main__":
    main()