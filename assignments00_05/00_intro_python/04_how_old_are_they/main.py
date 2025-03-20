def main():
    print("Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:\n")
    anton: int = 21
    beth: int = anton + 6
    chen: int = beth + 20
    drew: int = chen + anton
    ethan: int = chen

    print(f"Anton is {anton} years old.")
    print(f"Beth is {beth} years old.")
    print(f"Chen is {chen} years old.")
    print(f"Drew is {drew} years old.")
    print(f"Ethan is {ethan} years old.\n")



if __name__ == '__main__':
    main()