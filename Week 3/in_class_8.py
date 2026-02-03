# Children: $8, Senior: $10, Adult: $15
def main():
    age = int(input("Enter your age: "))

    if age <= 12:
        print("Your ticket price is $8")
    elif age >= 65:
        print("Your ticket price is $10")
    else:
        print("Your ticket price is $15")

if __name__ == "__main__":
    main()