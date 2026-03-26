def main():
    # At this point, `students` is a tuple
    students = ("John", 80.5)

    # At this point, `students` is a list
    students = list(students)

    students.append(90)

    print(students) # Notice this print statement, prints students as a list

    students = tuple(students)

    print(students) # Notice this print statement, prints students as a tuple

if __name__ == "__main__":
    main()