def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."

def print_length(lst):
    print(len(lst))


def add_item(lst, item):
    lst.append(item)

def print_list(lst):
    for item in lst:
        print(item)

def main():
    fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print("Current list:", fruit_lst)
    print("Choose an operation: \n1. access \n2. modify \n3. slice \n4. print \n5. length \n6. add \n7. exit")

    while True:
        operation = input("\n\033[1m\033[3mEnter operation: \033[0m")

        if operation == "access":
            index = int(input("\n\033[1mEnter index to access: \033[0m"))
            print(access_element(fruit_lst, index))
        elif operation == "modify":
            index = int(input("\n\033[1mEnter index to modify: \033[0m"))
            new_value = input("\033[1mEnter new value: \033[0m")
            print(modify_element(fruit_lst, index, new_value))
        elif operation == "slice":
            start = int(input("\n\033[1mEnter start index: \033[0m"))
            end = int(input("\033[1mEnter end index: \033[0m"))
            print(slice_list(fruit_lst, start, end))
        elif operation == "print":
            print_list(fruit_lst)
        elif operation == "length":
            print_length(fruit_lst)
        elif operation == "add":
            item = input("\n\033[1mEnter item to add: \033[0m")
            add_item(fruit_lst, item)
            print_list(fruit_lst)
        elif operation == "exit":
            break
        else:
            print("Invalid operation.")

if __name__ == "__main__":
    main()
