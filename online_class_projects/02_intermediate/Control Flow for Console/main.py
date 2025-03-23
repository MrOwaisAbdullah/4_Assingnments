import random

def main():
    print("\n\033[01m\033[03mWelcome to the Higher or Lower Game!\033[0m")

    score = 0

    for i in range(3):
        print("\n\033[01m\033[03mRound", i + 1, "\033[0m")
        print("\n\033[33mI am thinking of a number between 1 and 100...\033[0m\n")
        comp_rand = random.randint(1, 100)

        while True:
            user_guess = input("\n\033[01m\033[03mEnter Your number: \033[0m")
            if user_guess.isdigit():
                user_guess = int(user_guess)
                if user_guess > 100:
                    print("\033[93mPlease Enter a Number Between 1 and 100!\033[0m")
                else:
                    user_guess = int(user_guess)
                    break
            else:
                print("\033[93mPlease Enter a Valid Number!\033[0m")

        guessed_num = input("\n\033[01m\033[03mDo you think your number is higher or lower than the computer's? (h/l): \033[0m")
        while guessed_num not in ["h", "l"]:
            print("\033[93mPlease Enter a Valid Response!\033[0m")
            guessed_num = input("\n\033[01m\033[03mDo you think your number is higher or lower than the computer's? (h/l): \033[0m")
        
        if guessed_num == "h":
            if user_guess > comp_rand:
                print(f"\033[92mYou were right! The computer's number was \033[01m{comp_rand}.\033[0m")
                score += 1
                print(f"""\n\033[01m\033[03mYour Score: \033[03m{score}\033[0m""")
            else:
                print(f"\033[91mAww, that's incorrect. The computer's number was \033[01m{comp_rand}.\033[0m")
                print(f"""\n\033[01m\033[03mYour Score: \033[03m{score}\033[0m""")

        if guessed_num == "l":
            if user_guess < comp_rand:
                print(f"\033[92mYou were right! The computer's number was \033[01m{comp_rand}.\033[0m")
                score += 1
                print(f"""\n\033[01m\033[03mYour Score: \033[03m{score}\033[0m""")
            else:
                print(f"\033[91mAww, that's incorrect. The computer's number was \033[01m{comp_rand}.\033[0m")
                print(f"""\n\033[01m\033[03mYour Score: \033[03m{score}\033[0m""")

        
        print("\n---------------------------------------------------------------------------------\n")
    
    if score == 3:
        print("\033[92m\033[01mCongratulations! You got all the numbers right!\033[0m")
    elif score == 2:
        print("\033[92m\033[01mGood job! You got two numbers right!\033[0m")
    elif score == 1:
        print("\033[92m\033[01mNice try! You got one number right!\033[0m")
    else:
        print("\033[91m\033[01mBetter luck next time! You didn't get any numbers right.\033[0m")

    print("\n\033[01m\033[03mThanks for playing!\033[0m\n")

if __name__ == "__main__":
    main()