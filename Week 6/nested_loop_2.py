def main():
    counter = 0

    # for i in range(100):
    #     counter += 1

    for i in range(5):
        for y in range(2):
            for x in range(3):
                counter += 1 

    print(f"Counter: {counter}")


if __name__ == "__main__":
    main()