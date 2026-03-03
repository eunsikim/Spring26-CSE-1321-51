def my_function(num1, num2):
    num4 = num1 + num2
    # return will "return" a value
    return num4

def my_other_function(x):
    return x * 4

def main():
    num1 = 5
    num2 = 6

    # Method calls are expressions
    my_return_1 = my_function(num1, my_other_function(num2))
    print(my_return_1)

    print(my_other_function(num1) / 10)



if __name__ == "__main__":
    main()