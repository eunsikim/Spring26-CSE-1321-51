def main():
    # An integer at this point in the code
    my_number = 10
    print(my_number)

    # A float at this point in the code
    my_number = float(my_number)
    print(my_number)

    # When going from int to float, we cull
    my_number = 10.50
    my_number = int(my_number)
    print(my_number)

    my_string_number = "12.4"
    my_int_number = float(my_string_number)
    print(my_int_number)

    my_int_number = str(my_int_number)
    print(my_int_number)

if __name__ == "__main__":
    main()