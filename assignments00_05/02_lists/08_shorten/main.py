MAX_LENGTH = 5

def shorten(lst):
    return lst[:MAX_LENGTH]

def main():

    my_list = []
    while True:
        elem: str = input("Please enter an element of the list or press enter to stop. ")
        if elem == "":
            break
        my_list.append(elem)
    print(f"\n\033[3mOriginal List: {my_list}\033[0m\n")

    print(f"\n\033[3mShorten List: {shorten(my_list)}\033[0m\n")

if __name__ == '__main__':
    main()