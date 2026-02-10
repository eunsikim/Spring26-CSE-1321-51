def main():
    order = "Menu 2"

    # ==
    match order:
        case "Menu 1":
            print("Burger with Soda")
        case "Menu 2":
            print("Chicken strips with Soda")
        #Default case
        case _:
            print("We don't have that")

if __name__ == "__main__":
    main()