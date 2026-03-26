def average(*grades):
    sum_grades = 0

    for grade in grades:
        sum_grades += grade

    return sum_grades / len(grades)

def main():
    print(average(90, 70, 80.5, 60, 90, 91, 100))

if __name__ == "__main__":
    main()
