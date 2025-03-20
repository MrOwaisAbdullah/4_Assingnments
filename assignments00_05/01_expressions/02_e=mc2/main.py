def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def main():
    print("Find the Enery of a Mass using E=mc^2\n")
    while True:
        mass = input("\033[1m\033[3mEnter the mass in kg:\033[0m\n")
        if is_float(mass):
            break
        else:
            print("\033[91m\033[1m\033[4mError:\033[0m\033[91m Please enter a valid number.\033[0m\n")

    speed_of_light: float = 299792458 
    energy: float = float(mass) * speed_of_light ** 2

    print("\n\033[1m\033[3mResults:\033[0m\n")
    print("e = m * C^2...")
    print("m = " + str(mass) + " kg")
    print("C = " + str(speed_of_light) + " m/s\n")
    print(f"The energy of a mass of {mass} kg is {energy} joules of energy!\n")

if __name__ == "__main__":
    main()