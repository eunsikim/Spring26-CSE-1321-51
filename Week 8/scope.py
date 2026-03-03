def my_function(num1, num2):
    num3 = num1 + num2

    # We have an error because
    # num4 does not exist in my_function
    num3 *= num4
    print(num3)

def main():
    # num4 only "exists" whithin the
    # the main function
    num4 = 10
    my_function(5, 6)

    my_function(4, 2)

    my_function(6, 7)

    # print(num3 * 3)

if __name__ == "__main__":
    main()