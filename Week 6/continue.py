def main():
    counter = 0

    while True:
        if counter == 100:
            break
        elif counter % 2 == 0: #Check if counter is even (divisible by 2)
            counter += 1
            continue

        print(counter)
        counter += 1

if __name__ == "__main__":
    main()