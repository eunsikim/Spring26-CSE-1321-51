def main():
    username_data = "admin"
    password_data = "123"

    tries = 3

    while tries > 0:
        username_input = input("Username: ")
        password_input = input("Password: ")

        if username_input == username_data and password_input == password_data:
            print("Login Successful!")
            break
        else:
            tries = tries - 1
            print(f"Login information incorrect, you have {tries} tries left")
            # tries -= 1


if __name__ == "__main__":
    main()