# PURPOSE: Check/Validate user login
# INPUT/PARAMS: username and password
# PROCESS: Check if username and password are valid
# OUTPUT: TRUE if valid, FALSE if not valid
def validate(username, password):
    admin_username = "admin"
    admin_passowrd = "123"

    if username == admin_username and password == admin_passowrd:
        return True
    else:
        return False

# PURPOSE: Attempt to log-in the user
# INPUT/PARAMS: None
# PROCESS: Attempt 3 times to login the user
# OUTPUT: Return True if login succesfull, Return False if 
#         all attempts are used
def login():
    tries = 3

    while tries > 0:
        username_input = input("Username: ")
        password_input = input("Password: ")

        isValid = validate(username_input, password_input)

        if isValid:
            return True
        else:
            tries = tries - 1
            print(f"Login information incorrect, you have {tries} tries left")
    
    return False


def main():
    isLoggedIn = False

    print("1 to log-in")
    option = int(input("> "))

    if option == 1:
        isLoggedIn = login()

        if isLoggedIn:
            print("Login Succesful")

if __name__ == "__main__":
    main()