def main():
    students = []

    students.append( ["John", 80.5] )

    print(students)

    student_name = input("Name: ")
    student_grade = float(input("Grade: "))

    students.append( [student_name, student_grade] )

    print(students)

    students[0] = ["John", 100]

    print(students)

    students[0][0] = "Dave"

    print(students)

    del students[1]

    print(students)

    students.append(["Abigail", 90])

    students[1].clear()

    print(students)

if __name__ == "__main__":
    main()