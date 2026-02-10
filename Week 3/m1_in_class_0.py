def main():
    # Print prompt, read the input as a String, convert String to a Float, assign converted value to variable
    earth_weight = float( input("Enter your weight (in earth): ") )

    moon_weight = earth_weight * (16.5 / 100)

    print(f"Your moon weight is {moon_weight}")

if __name__ == "__main__":
    main()