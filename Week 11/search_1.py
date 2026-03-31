def main():
    my_numbers = [5, 4, 3, 9, 1]

    target = 7

    found = False

    counter = 1

    # Linear Search Algorithm
    # We go through each value one at a time
    # and check if the current value in the list
    # matches our target
    for number in my_numbers:
        if target == number:
            print(f"{target} exists in the list")
            print(f"It took me {counter} repetitions")
            found = True
            break
        else:
            counter += 1
        
    if found == False:
        print(f"{target} does not exists in the list")

if __name__ == "__main__":
    main()