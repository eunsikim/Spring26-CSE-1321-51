# Children: $8, Senior: $10, Adult: $15
def main():
    age = int(input("Enter your age: "))
    time = input("Is the movie after 4:00 PM (Y/N): ")

    if age <= 12:
        ticke_price = 8.0
        if time == 'N':
            ticke_price -= 2
    elif age >= 65:
        ticke_price = 10.0
        if time == 'N':
            ticke_price -= 2
    else:
        ticke_price = 15.0
        if time == 'N':
            ticke_price -= 2
    
    print(f"Your ticket price is ${ticke_price}")

if __name__ == "__main__":
    main()