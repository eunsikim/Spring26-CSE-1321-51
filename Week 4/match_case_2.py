def main():
    menuOrder = 10.0

    match menuOrder:
        # If you have the same case of the same parent data type (numerical)
        # The program executes the case nearest to the top
        case 10.0:
            print("Hello World")
        case 10:
            print("We do not sell integers")
        case "10":
            print("We may have some strings")
        case "burger":
            print("You ordered a burger")
        case "fries":
            print("You ordered fries")
        case "drink":
            print("You ordered a drink")
        case _:
            print("We do not have that item")


if __name__ == "__main__":
    main()