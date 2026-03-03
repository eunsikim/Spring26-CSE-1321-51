def my_function(num1, num2, num3 = 5):
    num4 = num1 + num2 * num3
    # return will "return" a value
    return num4

    print("Hello World")

def is_equal_to_5(x):
    if x == 5:
        # return will stop/break the function
        return True
    return False

def hello_world():
    print("Hello World")
    # This function returns `None` by default
    # Whenever you do not specify a return statement
    # python will, by default, add a return None

def main():
    num1 = 5
    num2 = 6
    num3 = 2

    my_return_1 = my_function(num1, num2) # int 35
    print(my_return_1)

    print(my_function(num1, num2, num3)) # int 17

    print(is_equal_to_5(4))
    print(is_equal_to_5(5))

    hello_world()
    print(type(hello_world()))
    print(type(my_function(num1, num2)))


if __name__ == "__main__":
    main()