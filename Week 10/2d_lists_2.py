def main():
    students = [["John", 80.5], ["Abigail", 90], ["Dave", 70], ["Daniel", 50]]
    
    # To access an element in a list of list
    # We specify which sublist we want to access
    # then, we specify which element of that sublist
    # we want access
    print(students[1][1])

    sublist_i = 0

    while sublist_i < len(students):
        data_i = 0
        while data_i < 2:
            print(f"{students[sublist_i][data_i]}", end=" ")
            data_i += 1
        print()
        sublist_i += 1

    # The code above works similarly to this:
    print(f"{students[0][0]} {students[0][1]}")
    print(f"{students[1][0]} {students[1][1]}")
    print(f"{students[2][0]} {students[2][1]}")
    # But it a more flexible and "automated" way.

if __name__ == "__main__":
    main()