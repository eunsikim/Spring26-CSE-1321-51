def main():
    student_age = [20, 18, 19]

    student_num = 1

    for student in student_age:
        print(f"Student {student_num} is {student} years old.")
        student_num += 1

    print(student_age[3])

if __name__ == "__main__":
    main()