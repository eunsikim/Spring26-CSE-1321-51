# Create a function that takes in a temperature value in Fahrenheit 
# which then converts it to celsius and returns it.
# c = 5/9 * (f - 32)
def f_to_c(f):
    return 5 / 9 * (f - 32)

# Create a function that takes in a temperature value in Celsius
# and returns `True` if the value is above 38, otherwise returns `False`
def is_fever(temp):
    if temp > 38:
        return True
    else:
        return False

# Create a function that takes in a boolean value and prints either
# `"Go to doctor"` or `"You are healthy"` based on the parameter value.
def get_medical_advice(fever):
    if fever == True:
        print("Go to doctor")
    else:
        print("You are healthy")

# CHALLENGE: In the main method, using a single line of code, get prompt and read
# the user's temperature and call the above functions to get the program to output 
# whether the user is healthy or if the user should go to the doctor.
def main():
    get_medical_advice(is_fever(f_to_c(float(input("Enter your temperature in F: ")))))

if __name__ == "__main__":
    main()