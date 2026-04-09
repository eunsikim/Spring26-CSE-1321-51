# This function takes in a list
# and returns a number which the average of that list
def average(grades):
    sum_grades = 0

    for grade in grades:
        sum_grades += grade

    return sum_grades / len(grades)

def main():
    students = {
        "John": {
            "Labs": [62, 73, 9, 76, 5, 49, 71, 26, 44, 89, 79, 23, 96],
            "Assignments": [9, 46, 47, 53, 48, 16, 29],
            "Midterm": 80,
            "Final": 81
        }
    }

    lab_avg = average(students["John"]["Labs"])
    assignment_avg = average(students["John"]["Assignments"])

    final_grade = lab_avg * 0.1 + assignment_avg * 0.4 + students["John"]["Midterm"] * 0.2 + students["John"]["Final"] * 0.3

    print(f"John has a final grade of {final_grade}")   

if __name__ == "__main__":
    main()