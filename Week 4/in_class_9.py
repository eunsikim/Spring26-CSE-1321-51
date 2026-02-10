# If Premium member or <$75 free shipping
def main():
    subtotal = float(input("Enter the subtotal: $"))
    isMember = input("Are you a member (Y/N): ") == "Y"

    if isMember == True:
        shipping = 0
    elif subtotal >= 75:
        shipping = 0
    else:
        shipping = 10

    print(f"Subtotal: ${subtotal}\nShipping Fee: ${shipping}\nTotal: ${subtotal + shipping}")


if __name__ == "__main__":
    main()