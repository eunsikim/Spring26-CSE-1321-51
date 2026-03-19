import random

def main():
    message = "Hello World"

    print(random.choice(message))

    # WE HAVE NOT COVERED LIST YET
    # THIS IS FOR EXAMPLE PURPOSES

    com_choice = ["rock", "paper", "scissors"]

    print(f"The computer chose {random.choice(com_choice)}")

if __name__ == "__main__":
    main()