def main():
    # Square
    # We build the vertical
    for y in range(5):
        # We build the row (horizontal line)
        for x in range(5):
            print("0", end="")
        print("")
    print()

    # Right Triangle
    num_of_zero = 1
    for y in range(5):
        for x in range(num_of_zero):
            print("0", end="")
        num_of_zero += 1
        print("")

    print()

    # Square
    # We build the vertical
    for y in range(5): # Range 0, 1, 2, 3, 4
        # We build the row (horizontal line)
        for x in range(5):
            print(y, end="")
        print("")

    print()

    # Square
    counter = 0
    for y in range(5): # Range 0, 1, 2, 3, 4
        # We build the row (horizontal line)
        for x in range(5):
            print(counter, end="")
            counter += 1
        print("")

if __name__ == "__main__":
    main()