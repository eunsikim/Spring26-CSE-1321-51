# Make sure the program does not crash when the program performs a division
# where `num2` has the value of `0`
def main():
    restart = "Y"

    while restart == "Y":
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

        # Input Validation
        # Keep prompting the user for an answer until 
        # the user enters a valid value: 'Y' or 'N'
        while True:
            restart = input("Do you want to perform another calculation (Y/N): ")

            if restart != "Y" and restart != "N":
                print("Please enter 'Y' for yes or 'N' for no")
            else:
                break

        


if __name__ == "__main__":
    main()