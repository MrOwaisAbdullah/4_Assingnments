PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    while True:
        age = input("\n\033[5m\033[34mPlease enter your age: \033[0m\n")
        if age.isdigit():
            age = int(age)
            if age > 0:
                break
            else:
                print("I Think you are not born yet! 😆")
        else:
            print("\033[3m\033[31mPlease enter a valid age!\033[0m\n")

    print("\n")
    if age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo, where the voting age is {PETURKSBOUIPO_AGE}!")
    if age >= STANLAU_AGE:
        print(f"You can vote in Stanlau! where the voting age is {STANLAU_AGE}!")
    if age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua, where the voting age is {MAYENGUA_AGE}!\n")
    if age < PETURKSBOUIPO_AGE:
        print(f"You cannot vote in Peturksbouipo, The voting age is {PETURKSBOUIPO_AGE}!")
    if age < STANLAU_AGE:
        print(f"You cannot vote in Stanlau, The voting age is {STANLAU_AGE}!")
    if age < MAYENGUA_AGE:
        print(f"You cannot vote in Mayengua, The voting age is {MAYENGUA_AGE}!\n")

if __name__ == '__main__':
    main()