def get_user_info():
    n = input("Enter your name: ")
    a = int(input("Enter your age: "))

    # You can return more than 1 value in a function
    # The following return will return the name and age
    # as a tuple.
    return n, a

def main():
    # You can "Pair" each return value to variable
    name, age = get_user_info()

    print(f"Your name is {name}, and your are {age} years old.")


if __name__ == "__main__":
    main()