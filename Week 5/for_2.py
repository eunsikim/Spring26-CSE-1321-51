def main():
    # Whenever we give range() one value,
    # It starts with 0 and the END range is 
    # always exclusive
    print("Range with one value:")
    for x in range(5):
        print(f"x = {x}")
    print()

    # Whenever we give range() two numbers
    # (Separated by a comma `,`):
    # Start is always inclusive
    # End is always exclusive
    print("Range with two values:")
    for x in range(0, 10 + 1):
        print(f"x = {x}")
    print()

    # Whenever we givve range() three numbers
    # The third value is the STEP
    # the difference between each number in the sequence
    print("Range with three values:")
    for x in range(0, 11, 2):
        print(f"x = {x}")
    print()

    for x in range(10, 0, -1):
        print(f"x = {x}")
        


if __name__ == "__main__":
    main()