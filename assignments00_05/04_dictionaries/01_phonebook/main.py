def phone_numbers(phonebook):
    while True:
        name = input("\033[03mName: \033[0m")
        if name == "":
            break
        number = input("\033[03mNumber: \033[0m")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def lookup_numbers(phonebook):
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])


def main():
    print("\033[01m\033[03mPhonebook\033[0m")
    print("\033[01m\033[03m---------\033[0m")
    print("1. Add to Phonebook")
    print("2. View Phonebook")
    print("3. Lookup Number")
    print("4. Exit")

    phonebook = {}
    while True:
        choice = input("\nEnter choice from 1-4: \n")
        if choice == "1":
            phone_numbers(phonebook)
        elif choice == "2":
            print_phonebook(phonebook)
        elif choice == "3":
            lookup_numbers(phonebook)
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()