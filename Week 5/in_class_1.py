# Create a password validation program
# The program should ask the user to input a password
# then validate/check if the password is valid or not

# Password rules:
# - A password must contain at least one number
# - A password must contain at least 8 or more characters

def main():
    password = input("Enter a password: ")

    hasNumber = False

    for c in password:
        if c == "0" or c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9":
            hasNumber = True
            break

    for ...
    
    if hasNumber:
        print("The password is valid")
    else:
        print("The password is not valid")

if __name__ == "__main__":
    main()