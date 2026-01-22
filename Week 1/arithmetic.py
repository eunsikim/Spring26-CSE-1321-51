def main():
    number1 = 10.0
    number2 = 4

    # If one operand is a float, it yields a float.
    # Otherwise, it yields an int.
    addition = number1 + number2
    subtraction = number1 - number2
    multiplication = number1 * number2
    power = number1 ** number2

    # Except division, it is always a float
    division = number1 / number2

    # If one operand is a float, it yields a float.
    # Otherwise, it yields an int.
    floor_div = number1 // number2
    print(floor_div)
    modulus = number1 % number2
    print(modulus)


    # print(number1 > number2)
    # print(number1 < number2)
    # print(number1 == number2)
    # print(number1 != number2)

    print(number1 != number2 and number1 < number2)

if __name__ == "__main__":
    main()