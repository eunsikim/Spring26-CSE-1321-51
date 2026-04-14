class section:
    def __init__ (self, section_num):
        self.students = []
        self.section_num = section_num

        print(f"Creating CSE 1321L Section {section_num}")

        # As soon the constructor function is called, we ask the user
        # to input the students
        while True:
            name = input("> ")

            if name == "-1":
                break

            labs_str = input("> ").split(", ")
            labs_float = []

            for val in labs_str:
                labs_float.append(float(val))

            assignments_str = input("> ").split(", ")
            assignments_float = []

            for val in assignments_str:
                assignments_float.append(float(val))

            exams_str = input("> ").split(", ")
            exams_float = []

            for val in exams_str:
                exams_float.append(float(val))
            
            self.students.append(student(name, assignments_float, labs_float, exams_float))

    def get_class_avg(self):
        class_avg = 0

        for st in self.students:
            class_avg += st.get_final_grade()
        
        return class_avg / len(self.students)

    def print_final_grades(self):
        for st in self.students:
            print(f"{st.name} has a final grade of {st.get_final_grade():.2f}")

class student:
    def __init__(self, name, assignments, labs, exams):
        self.name = name
        self.assignments = assignments
        self.labs = labs
        self.exams = exams
    
    def get_final_grade(self):
        lab_avg = 0
        assignment_avg = 0
        midterm_exam = self.exams[0]
        final_exam = self.exams[1]

        for lab_grade in self.labs:
            lab_avg += lab_grade
        
        lab_avg = lab_avg / len(self.labs)

        for assignment_grade in self.assignments:
            assignment_avg += assignment_grade
        
        assignment_avg = assignment_avg / len(self.assignments)

        return lab_avg * 0.1 + assignment_avg * 0.4 + midterm_exam * 0.2 + final_exam * 0.3

def main():
    my_sections = []
    

    my_sections.append(section("51"))
    print()

    my_sections.append(section("05"))

    print()
    print(f"Section {my_sections[0].section_num} class avg {my_sections[0].get_class_avg()}")
    my_sections[0].print_final_grades()
    print()
    print(f"Section {my_sections[1].section_num} class avg {my_sections[1].get_class_avg()}")
    my_sections[1].print_final_grades()
    

if __name__ == "__main__":
    main()