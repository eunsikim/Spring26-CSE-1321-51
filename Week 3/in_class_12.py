# Make sure the program does not crash when the program performs a division
# where `num2` has the value of `0`
def main():
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    op = input("What operation do you want to perform (+, -, *, /): ")

    match op:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            result = num1 / num2
    
    print(f"{num1} {op} {num2} = {result}")
        


if __name__ == "__main__":
    main()