def count_nums(num_list):
    num_dict = {}
    for num in num_list:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    return num_dict

def main():
    num_list = []
    while True:
        num = input("\n\033[01m\033[03mEnter a Number: \033[0m\n")
        if not num:
            break
        else:
            if num.isdigit():
                num = int(num)
                num_list.append(num)
            else:
                print("Please Enter a Valid Number!")
    num_dict = count_nums(num_list)

    for key, value in num_dict.items():
        print(f"\033[01m\033[03m{key}\033[0m appears \033[01m\033[03m{value}\033[0m times.", end=" ")
        
if __name__ == "__main__":
    main()
