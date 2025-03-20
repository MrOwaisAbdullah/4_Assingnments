def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def main():
    print("\nType two numbers to Find there Sum.\n\n")

    while True:
        num1 : float = input("Enter first number: ")
        if is_float(num1):
            break
        else:
            print("Please Enter a Number!!!")

    while True:
        num2 : float = input("Enter second number: ")
        if is_float(num2):
            break
        else:
            print("Please Enter a Number!!!")

    total : float = float(num1) + float(num2)
    print(f"The total is {str(total)}\n")

if __name__ == '__main__':
    main()