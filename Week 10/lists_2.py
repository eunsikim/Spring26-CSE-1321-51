def main():
    student_age = []

    while True:
        age = int(input("Enter an age or -1 to stop: "))

        if age == -1:
            break
        
        # Add a value at the END of the list
        student_age.append(age)
        # `insert()` add a new value at a specific index

    print(student_age[3])

    student_num = 1

    for student in student_age:
        print(f"Student {student_num} is {student} years old.")
        student_num += 1

if __name__ == "__main__":
    main()