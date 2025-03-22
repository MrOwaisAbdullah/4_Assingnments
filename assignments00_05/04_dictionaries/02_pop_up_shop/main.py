def main():
    fruits = {'apple': 20, 'cherry': 20, 'banana': 10, 'kiwi': 50, 'grapes': 2, 'mango': 30}
    
    total_cost = 0
    for fruit_name, price in fruits.items():
        while True:
            amount_bought = input(f"\nHow many \033[01m\033[03m({fruit_name})\033[0m do you want to buy? ")
            if amount_bought.isdigit():
                amount_bought = int(amount_bought)
                break
            else:
                print("Please Enter a Valid Quantity!")
        total_cost += (price * amount_bought)
    
    print(f"\nYour total is PKR {str(total_cost)}/-")


if __name__ == '__main__':
    main()