def main():
    # input() always resolves to string
    age = int(input("Enter your age: "))

    print("10 Years pass by...")

    age = age + 10

    print(age)

if __name__ == "__main__":
    main()