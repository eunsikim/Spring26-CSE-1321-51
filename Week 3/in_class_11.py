# Change the program so it accepts both digit and written (lowercase) number
# Ex: "3" or "three"
# The match case statement (ln. 7) must have only 4 cases and a default case
def main():
    num_sides = input("Enter the number of sides: ")

    match num_sides:
        case "three":
            print("This is a triangle")
        case "four":
            print("This is a quadrilateral")
        case "five": 
            print("This is a pentagon")
        case "six":
            print("This is a hexagon")
        case _:
            print("I do not know")
        


if __name__ == "__main__":
    main()