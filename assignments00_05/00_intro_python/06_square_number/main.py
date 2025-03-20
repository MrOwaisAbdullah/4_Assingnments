def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def main():
    print("Find the Square of a Number\n")

    while True:
        num = input("\033[1m\033[3mType a number to see the square\033[0m \n")
        if is_float(num):
            break
        else:
            print("Input Value should be a number!!!\n")

    num_square = float(num) ** 2
    print(f"The square of {num} is {num_square}.\n")


if __name__ == '__main__':
    main()