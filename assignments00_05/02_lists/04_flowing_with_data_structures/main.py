def add_three_copies(list_items, data):
    for _ in range(3):
        list_items.append(data)

my_list = []

def main():
    message = input("\033[1m\033[3mEnter a message to copy: \033[0m\n")
    print(f"\nList before: {my_list}")
    add_three_copies(my_list, message)
    print(f"\nList after: {my_list}\n")

if __name__ == "__main__":
    main()