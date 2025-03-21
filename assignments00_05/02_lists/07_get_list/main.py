def main():
    my_list = []

    while True:
        elem: str = input("Please enter an element of the list or press enter to stop. ")
        if elem == "":
            break
        my_list.append(elem)
    print(f"\n\033[3mYour List: {my_list}\033[0m\n")


if __name__ == '__main__':
    main()