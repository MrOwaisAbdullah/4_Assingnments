PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you:\n\nSophia is heading out to the grocery store.\nA programmer tells her: get a liter of milk, and if they have eggs, get 12.\n\nSophia returns with 13 liters of milk.\nThe programmer asks why and Sophia replies: 'because they had eggs'"
SORRY: str = "Sorry I only tell jokes."

def main():
    user_input = input(f"\n\033[1m{PROMPT}\033[0m")
    user_input = user_input.strip().lower()
    
    if user_input == "joke":
        print(f"\n{JOKE}\n")
    else:
        print(f"\n{SORRY}\n")

if __name__ == "__main__":
    main()