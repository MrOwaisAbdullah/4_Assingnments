def main():
    num_list = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8]

    for num in range(len(num_list)):
        num_list[num] *= 2

    print(num_list)
        
if __name__ == "__main__":
    main()