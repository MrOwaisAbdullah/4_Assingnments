MERCURY_GRAVITY = 0.376 
VENUS_GRAVITY = 0.889 
MARS_GRAVITY = 0.378 
JUPITER_GRAVITY = 2.36 
SATURN_GRAVITY = 1.081 
URANUS_GRAVITY = 0.815 
NEPTUNE_GRAVITY = 1.14 
EARTH_GRAVITY = 1.0


def main():
    while True:
        earth_weight = input("\n\033[1mEnter a weight on Earth: \033[0m\n")
        if earth_weight.isdigit():
            earth_weight = float(earth_weight)
            if earth_weight > 0:
                break
        else:
            print("Please Enter a Valid Number!")
    
    print("Planets: \n1. Mercury \n2. Venus \n3. Mars \n4. Jupiter \n5. Saturn \n6. Uranus \n7. Neptune")
    
    while True:
        planet = input("\n\033[1mEnter a planet: \033[0m")
        planet = planet.lower()

        gravity_constant = ""

        if planet == "mercury":
            gravity_constant = MERCURY_GRAVITY
            break
        elif planet == "venus":
            gravity_constant = VENUS_GRAVITY
            break
        elif planet == "mars":
            gravity_constant = MARS_GRAVITY
            break
        elif planet == "jupiter":
            gravity_constant = JUPITER_GRAVITY
            break
        elif planet == "saturn":
            gravity_constant = SATURN_GRAVITY
            break
        elif planet == "uranus":
            gravity_constant = URANUS_GRAVITY
            break
        elif planet == "neptune":
            gravity_constant = NEPTUNE_GRAVITY
            break
        else:
            print("\033[91mInvalid planet\033[0m")

    planetary_weight = earth_weight * gravity_constant
    rounded_planetary_weight = round(planetary_weight, 2)

    print(f"\nYour weight on \033[1m{planet}\033[0m would be \033[1m{rounded_planetary_weight}.\033[0m\n")

if __name__ == "__main__":
    main()