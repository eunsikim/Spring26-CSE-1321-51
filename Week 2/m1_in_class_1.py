def main():
    # Print prompt, read the input as a String, convert String to a Float, assign converted value to variable
    temp_f = float( input("Enter a temperature (in F): ") )

    temp_k = (temp_f - 32) * 5 / 9 + 273.15

    print(f"Your temperature in Kelvin: {temp_k}K")

if __name__ == "__main__":
    main()