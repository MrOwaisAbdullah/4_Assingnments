MINIMUM_HEIGHT : int = 50

def main():
    while True:
        height = input("\n\033[01m\033[03mHow tall are you? \033[0m\n")
        if not height:
            break
        else:
            if height.isdigit():
                height = int(height)
                if height > 0:
                    break
            else:
                print("Please enter a valid height!\n")

    if height:
        if height >= MINIMUM_HEIGHT:
            print("\nYou're tall enough to ride!")
        else:
            print("\nYou're not tall enough to ride, but maybe next year!")



if __name__ == '__main__':
    main()