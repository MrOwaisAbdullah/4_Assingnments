from hashlib import sha256

# login function takes an email, a dictionary of stored logins, and a password to check as input
def login(email, stored_logins, password_to_check):
    if email in stored_logins:
        if stored_logins[email] == hash_password(password_to_check):
            return True    
    return False

# hash_password function takes a password as input and returns the hashed password
def hash_password(password):
    return sha256(password.encode()).hexdigest()

def add_login(email, password, stored_logins):
    stored_logins[email] = hash_password(password)
    return stored_logins

def enter_login():
    email = input("\n\033[01m\033[03mEnter email: \033[0m")
    password = input("\n\033[01m\033[03mEnter password: \033[0m")
    return email, password

# main function to test the login function
def main():
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    while True:
        choice = input("Enter choice: ")

        if choice == "1":
            email, password = enter_login()
            stored_logins = add_login(email, password, stored_logins)
            print("\n\033[92mRegistration successful\033[0m\n")
        elif choice == "2":
            email, password = enter_login()
            if login(email, stored_logins, password):
                print("\n\033[92mLogin successful\n\033[0m")
            else:
                print("\n\033[91mLogin failed\n\033[0m")
        elif choice == "3":
            break
        else:
            print("\n\033[91mInvalid choice\n\033[0m")

if __name__ == '__main__':
    main()