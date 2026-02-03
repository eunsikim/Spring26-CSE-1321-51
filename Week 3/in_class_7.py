# subtotal >= $100, then $20 off
# subtotal >= $50, then $5 off
def main():
    subtotal = float(input("Enter subtotal: $"))

    if subtotal >= 100:
        total = subtotal - 20
    elif subtotal >= 50:
        total = subtotal - 5
    else:
        total = subtotal

    print(f"Total is ${total}")

if __name__ == "__main__":
    main()