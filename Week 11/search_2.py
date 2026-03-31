def main():
    # Binary Search
    # We need to have a sorted list
    # We start looking into the middle value in the list
    # Then shift our focus in the list to the section
    # with higher chances to find the target
    my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    found = False

    target = 5

    low_index = 0
    high_index = len(my_numbers) - 1
    middle_index = int(len(my_numbers) / 2)

    counter = 1

    while low_index < high_index:
        if target == my_numbers[middle_index]:
            print(f"{target} exists in the list")
            print(f"It took me {counter} repetitions")
            found = True
            break
        elif target > my_numbers[middle_index]:
            low_index = middle_index
            middle_index = int((high_index - low_index) / 2) + middle_index
            print(middle_index)
            counter += 1
        elif target < my_numbers[middle_index]:
            high_index = middle_index
            middle_index = int((high_index - low_index) / 2)
            counter += 1

    if found == False:
        print(f"{target} does not exists in the list")


if __name__ == "__main__":
    main()