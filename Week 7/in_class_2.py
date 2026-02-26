# Create a function that TAKES IN 2 numeric values
# and checks if the first value is divisible by the second
# the function should PRINT if they are divisible or not.
def isDivisible(num1, num2):
    if num2 % num1 == 0:
        print(f"{num1} is divisible by {num2}")
    else:
        print(f"{num1} is not divisible by {num2}")

def main():
    isDivisible(2, 10)
    isDivisible(3, 10)
    isDivisible(4, 12)

if __name__ == "__main__":
    main()