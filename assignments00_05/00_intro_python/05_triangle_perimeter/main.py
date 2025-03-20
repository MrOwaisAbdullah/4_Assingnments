def main():
    print("Find the perimeter of the triangle!\n")
    while True:
        side_1 = input("\033[1m\033[3mWhat is the length of side 1?\033[0m \n")
        if side_1.isdigit():
            break
        else:
            print("Input Value should be a number!!!\n")

    while True:
        side_2 = input("\033[1m\033[3mWhat is the length of side 2?\033[0m \n")
        if side_2.isdigit():
            break
        else:
            print("Input Value should be a number!!!\n")

    while True:
        side_3 = input("\033[1m\033[3mWhat is the length of side 3?\033[0m \n")
        if side_3.isdigit():
            break
        else:
            print("Input Value should be a number!!!\n")

    triangle_perimeter: float = float(side_1) + float(side_2) + float(side_3)

    print(f"\nThe perimeter of the triangle is \033[1m{triangle_perimeter}\033[0m\n")

if __name__ == '__main__':
    main()