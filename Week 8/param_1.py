# num1 & num2 are required parameters
# num3 is our optional parameter
# therefore, num3 can have the value of 5
# when the call doesnt specify the third parameter

# NOTE: All optional params have to be defined after
# the required params.
# def my_function(num3 = 5, num1, num2):
def my_function(num1, num2, num3 = 5):
    num4 = num1 + num2 * num3
    print(num4)

def main():
    num1 = 5
    num2 = 6
    my_function(5, 6)
    my_function(5, 6, 2)


if __name__ == "__main__":
    main()