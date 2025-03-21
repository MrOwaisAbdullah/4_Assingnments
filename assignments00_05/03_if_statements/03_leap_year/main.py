def main():
    while True:
        year = input("\n\033[01mEnter a year: \033[0m\n")
        if year.isdigit():
            year = int(year)
            if year > 0:
                break
        else:
            print("Please Enter a Valid Year!")
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"\n\033[01m{year}\033[0m is a leap year.\n")
    else:
        print(f"\n\033[01m{year}\033[0m is not a leap year.\n")

if __name__ == "__main__":
    main()