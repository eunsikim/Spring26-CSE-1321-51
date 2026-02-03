# Children: $8, Senior: $10, Adult: $15
def main():
    age = int(input("Enter your age: "))
    time = input("Is the movie after 4:00 PM (Y/N): ")

    if age <= 12 and time == 'Y':
        print("Your ticket price is $8")
    elif age <= 12:
        print("Your ticket price is $6")
    elif age >= 65 and time == 'Y':
        print("Your ticket price is $10")
    elif age >= 65:
        print("Your ticket price is $8")
    elif time == 'Y': # At this point 12 > age < 65 and movie time is after 4 PM
        print("Your ticket price is $15")
    else: # At this point 12 > age < 65 and movie time is before 4 PM
        print("Your ticket price is $13")

if __name__ == "__main__":
    main()