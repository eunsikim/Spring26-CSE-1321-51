# In this new iteration of this project, we application will be able to handle multiple courses
# with different grading scheme (the old "version" of the application only worked for CSE 1321L)
# To accomplish this, we need to do several changes in the structure of the application.

# The `student` class cannot contain data regarding grades, at least not as object attributes.

# Instead, we will rely on a new class `student_grade` which will handle the grades of a single
# student within a single course.
# `student_grade` relies on a grading scheme, this will be in the form of a dictionary
# this dictionary/scheme will contain the grading information of a single course
# This class contains a student object as attribute to be able to "link" a student with a grade.
# Moreover, it has a scheme attribute which it uses to calculate the student's final grade and also
# to add the student's grade, keeping track of all of the grading items in a course.

# The `section` class now has been renamed `course` since it will contain information of any
# course in KSU. `course` has a couple of new attributes:
#   - gradebook: This list will contain `student_grade` objects. We will use this whenever
#                whenever we need to calculate or access a single student's grade.
#   - course_name: This attribute will store the course name
#   - grading_scheme: Since each course will have a different scheme, we track this information
#                     within a single `course` object.
# The insertion of students into a course now is handled in a separate function rather than
# in the constructor. This was done to make the code look cleaner, but it will require to
# call the `add_students()` function separately to add students.
# Notice how the `add_students()` appends to the students and gradebook attribute lists.
# students will be used to access each student, while gradebook will be used anytime we
# need to work on grades.
# To add grades, the `add_grades()` function iterates through the gradebook and calls the
# `student_grade` object's `add_grades()` function.

class course:
    def __init__(self, course_name, course_section, grading_scheme):
        self.students = []
        self.gradebook = []
        self.course_name = course_name
        self.course_section = course_section
        self.grading_scheme = grading_scheme

        print(f"{self.course_name} section {self.course_section} has been created.")

    def add_students(self):
        counter = 0
        while True:
            name = input("Enter student name or -1 to stop: ")

            if name == "-1":
                break
            
            new_student = student(name)

            self.students.append(new_student)
            self.gradebook.append(student_grade(new_student, self.grading_scheme))

            counter += 1

            print()

        print(f"{counter} students were added.")

    def add_grades(self):
        print(f"Adding grades for each students in {self.course_name} section {self.course_section}")
        for st in self.gradebook:
            st.add_grades()
    
    def print_final_grades(self):
        print(f"Final Grades for {self.course_name} section {self.course_section}:")
        for st in self.gradebook:
            print(f"{st.student.name} has a final grade of {st.get_final_grade():.2f}")
    
    def print_class_avg(self):
        class_sum = 0

        for st in self.gradebook:
            class_sum += st.get_final_grade()
        
        class_avg = class_sum / len(self.students)

        print(f"{self.course_name} Section {self.course_section} has an average class grade of {class_avg:.2f}")

    def print_classlist(self):
        print("Classlist:")
        for st in self.students:
            print(f"- {st.name}")
        
class student_grade:
    def __init__(self, student, scheme):
        self.student = student
        self.scheme = scheme
        self.grades = {}
    
    def add_grades(self):
        print(f"Adding grades for {self.student.name}")
        for item in self.scheme:
            if self.scheme[item]["is_average"] == True:
                print(f"\tEnter {self.scheme[item]["amount"]} {item} grades:")

                grade_list = []

                for i in range(self.scheme[item]["amount"]):
                    grade_value = float(input("\t> "))
                    grade_list.append(grade_value)
                
                self.grades[item] = grade_list
            else:
                print(f"\tEnter {item} grade")
                grade_value = float(input("\t> "))

                self.grades[item] = grade_value
            print()
    
    def get_final_grade(self):
        final_grade = 0
        for item in self.scheme:
            if self.scheme[item]["is_average"] == True:
                final_grade += self.get_avg(self.grades[item]) * self.scheme[item]["weight_percent"] / 100
            else:
                final_grade += self.grades[item] * self.scheme[item]["weight_percent"] / 100
        return final_grade

    def get_avg(self, grade_list):
        grade_list_sum = 0

        for grade in grade_list:
            grade_list_sum += grade
        
        return grade_list_sum / len(grade_list)


class student:
    def __init__(self, name):
        self.name = name

def CSE1321L_Grading_Scheme():
    scheme = {
        "Lab":{
            "is_average": True,
            "weight_percent": 10,
            "amount": 13
        },
        "Assignment":{    
            "is_average": True,
            "weight_percent": 40,
            "amount": 7
        },
        "Midterm exam":{
            "is_average": False,
            "weight_percent": 20
        },
        "Final exam":{
            "is_average": False,
            "weight_percent": 30
        }
    }

    return scheme

def CSE1321_Grading_Scheme():
    scheme = {
        "Quiz":{
            "is_average": True,
            "weight_percent": 25,
            "amount": 10
        },
        "Test 1":{    
            "is_average": False,
            "weight_percent": 25
        },
        "Test 2":{
            "is_average": False,
            "weight_percent": 25
        },
        "Final exam":{
            "is_average": False,
            "weight_percent": 25
        }
    }

    return scheme

def HIST2112_Grading_Scheme():
    scheme = {
        "Attendance":{
            "is_average": True,
            "weight_percent": 10,
            "amount": 32
        },
        "Discussion":{    
            "is_average": True,
            "weight_percent": 10,
            "amount": 7
        },
        "Quiz":{
            "is_average": True,
            "weight_percent": 30,
            "amount": 5
        },
        "Midterm exam":{
            "is_average": False,
            "weight_percent": 25
        },
        "Final exam":{
            "is_average": False,
            "weight_percent": 25
        }
    }

    return scheme


def main():
    cse1321 = course("CSE 1321", "05", CSE1321_Grading_Scheme())
    cse1321L = course("CSE 1321L", "W01", CSE1321L_Grading_Scheme())
    hist2112 = course("HIST 2112", "01", HIST2112_Grading_Scheme())

    courses = []
    courses.append(cse1321)
    courses.append(cse1321L)
    courses.append(hist2112)
    print()

    for c in courses:
        print(f"[{c.course_name} Section {c.course_section}]")
        c.add_students()
        print()
        c.print_classlist()
        print()
        c.add_grades()
        print()
        c.print_final_grades()
        print()
        c.print_class_avg()
        print()

    

if __name__ == "__main__":
    main()

        
        

        