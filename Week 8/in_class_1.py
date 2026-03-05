import random
# This line of code generates a random number from 1 to 100 => random.randint(0, 100)

# Create a function that takes in two parameters: the user's first name
# and the user's last name. The function generates a netID based on these
# values using the random module to generate a number for the id. The function
# returns the generated netID

# A valid netID is composed of the FIRST leter of the first name and UP TO the
# first 5 letters of the lastname, followed by a number.

# CREATE YOUR FUNCTION BELOW THIS COMMENT
def generate_netID(firstname, lastname):
    netID = firstname[0]

    counter = 1

    for char in lastname:
        if counter <= 5:
            netID += char
            counter += 1
    
    random_num = random.randint(0, 100)
    
    return f"{netID}{random_num}"



