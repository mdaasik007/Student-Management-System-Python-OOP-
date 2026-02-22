# Student Management System

# --- Inheritance
# Student --> Person
# Teacher --> Person

# -------- Inheritance --------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
        
    def __str__(self):
        return (
            f"Student Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Student ID: {self.student_id}\n"
            f"Course: {self.course}"
        )

        
class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject
    
    def __str__(self):
        return (
            f"Teacher Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Employee ID: {self.employee_id}\n"
            f"Subject: {self.subject}"
        )

# Aggrigation and composition

# Classroom Compostion : without school classroom cant exist

# -------- Composition --------

class ClassRoom:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        
    def __str__(self):
        return f"\nRoom NO: {self.room_number}\nCapacity: {self.capacity}"
    
# -------- Aggregation + Composition --------

class School:
    def __init__(self, school_name, location):
        self.school_name = school_name
        self.location = location
        self.students = []   # Aggregation
        self.teachers = []   # Aggregation
        self.class_room = [] # Composition
        
        # Aggregation methods
        
    def add_students(self, student):
        self.students.append(student)
        
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            
    def remove_teacher(self, teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)
            
            # Composition method
            
    def add_classroom(self, room_number, capacity):
        classrooms = ClassRoom(room_number, capacity)
        self.class_room.append(classrooms)
        
        
    # saving all details in single txt file
    
    def display(self):
        with open("Details.txt", "a") as f:
            f.write("School :" + str(self.school_name) + "\n")
            f.write("School Location :" + str(self.location) + "\n")
            
            f.write("Students:\n")
            for std in self.students:
                f.write(str(std) + "\n")
            f.write("\n")
            
            f.write("Teachers:\n")
            for ter in self.teachers:
                f.write(str(ter) + "\n")
            f.write("\n")
               
            f.write("ClassRoom :" )
            for room in self.class_room:
                f.write(str(room) + "\n")
            f.write("-----------------------\n")
            
        print("Details Created Successfully!")
        
        
# Class Objects

#Student objects
student1 = Student("Aasik", 19, 1231123, "AI & ML")
student2 = Student("Akbar", 20, 1102388, "AI & DS")
student3 = Student("Anwar", 19, 1231100, "IT")

# Teacher objects
teacher1 = Teacher("Abdul", 30, 1101110, "Python")
teacher2 = Teacher("Azmar", 26, 1101121, "JAVA")
teacher3 = Teacher("Abdul", 38, 1101122, "ML")

#School Object
school1 = School("HISAC", "CBE")
school2 = School("HICAS", "CBE")

# Composition (School creates classrooms)
school1.add_classroom(101, 40)
school1.add_classroom(102, 35)

school2.add_classroom(201, 50)

# Aggregation (Pass existing objects)
# Accesing Methods

#Adding Students
school1.add_students(student1)
school1.add_students(student2)
school2.add_students(student3)

# Adding teachers
school1.add_teacher(teacher1)
school1.add_teacher(teacher2)
school2.add_teacher(teacher3)

school1.display()
school2.display()