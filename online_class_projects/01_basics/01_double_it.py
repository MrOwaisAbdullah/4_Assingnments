def main():
    while True:
        curr_value = input("\n\033[1m\n\033[3mEnter a number: \n\033[0m")
        if curr_value.isdigit():
            curr_value = int(curr_value)
            if curr_value > 0:
                break
        else:
            print("Please Enter a Valid Number!")

    while curr_value < 100:
        curr_value *= 2
        print(curr_value, end=" ")
    print("\n")

if __name__ == "__main__":
    main()