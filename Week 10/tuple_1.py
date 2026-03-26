def main():
    students = ("John", 80.5)

    my_list = []

    print(students)

    print(students[1])

    for value in students:
        print(value)

    # We cannot modify/update values in a tuple
    # students[0] = "Dave"

    # We cannot add values into a tuple (This function does not exist)
    # students.append(80)

    # We cannot delete a value in a tuple
    # del students[0]

if __name__ == "__main__":
    main()