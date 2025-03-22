AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print(f"\nPlease type the following affirmation: \033[36m{AFFIRMATION}\033[0m")

    user_feedback = input() 
    while user_feedback != AFFIRMATION:
        print("\n\033[93mThat was not the affirmation.\033[0m")

        print(f"\nPlease type the following affirmation: \033[33m{AFFIRMATION}\033[0m")
        user_feedback = input()

    print("\n\033[92mThat's right! :)\033[0m")
    print("You are capable of doing anything you put your mind to.\n")

if __name__ == '__main__':
    main()