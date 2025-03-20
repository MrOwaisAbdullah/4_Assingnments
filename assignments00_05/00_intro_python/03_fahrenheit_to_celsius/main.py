def main():
    print("Farenheit to Celcius Converter!\n")
    while True:
        degrees_fahrenheit = input("\033[1m\033[3mEnter Farenheit to convert:\033[0m \n")
        if degrees_fahrenheit.isdigit():
            break
        else:
            print("Input Value should be a number!!!\n")

    print("\n")
    degrees_celsius: float = (float(degrees_fahrenheit) - 32) * 5.0/9.0

    print(f"{degrees_fahrenheit}F is equals to {degrees_celsius}C\n")


if __name__ == "__main__":
    main()