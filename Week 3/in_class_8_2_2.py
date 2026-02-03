# Children: $8, Senior: $10, Adult: $15
def main():
    age = int(input("Enter your age: "))
    time = input("Is the movie after 4:00 PM (Y/N): ")

    if age <= 12:
        if time == 'Y':
            print("Your ticket price is $8")
        else:
            print("Your ticket price is $6")
    elif age >= 65:
        if time == 'Y':
            print("Your ticket price is $10")
        else:
            print("Your ticket price is $8")
    else:
        if time == 'Y':
            print("Your ticket price is $15")
        else:
            print("Your ticket price is $13")

if __name__ == "__main__":
    main()