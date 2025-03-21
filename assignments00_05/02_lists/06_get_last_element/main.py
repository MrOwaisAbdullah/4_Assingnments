def get_last_element(my_list):
    print(f"\033[3m\nHere is the Last Element of the List: \033[5m{my_list[-1]}\033[0m\n")

def main():
    my_list = []

    while True:
        elem: str = input("Please enter an element of the list or press enter to stop. ")
        if elem == "":
            break
        my_list.append(elem)
    
    get_last_element(my_list)


if __name__ == '__main__':
    main()