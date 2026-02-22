🎓 Student Management System (Python OOP)

A simple Student Management System built using Object-Oriented Programming (OOP) concepts in Python.

This project demonstrates:

✅ Inheritance (IS-A relationship)

✅ Aggregation (HAS-A weak relationship)

✅ Composition (HAS-A strong relationship)

✅ File Handling (Saving details to .txt file)

📌 OOP Concepts Used
🔹 1. Inheritance (IS-A Relationship)

Student is a Person

Teacher is a Person

        Person
        /    \
   Student   Teacher
🔹 2. Aggregation (HAS-A Weak Relationship)

School has Students

School has Teachers

Students and Teachers can exist independently of School

🔹 3. Composition (HAS-A Strong Relationship)

School has ClassRoom

Classroom cannot exist without School

🏗️ Class Structure
👤 Person (Base Class)
Attribute	Type
name	str
age	int
🎓 Student (Inherits Person)
Attribute	Type
student_id	int
course	str

Methods:

__str__() → Returns formatted student details

👨‍🏫 Teacher (Inherits Person)
Attribute	Type
employee_id	int
subject	str

Methods:

__str__() → Returns formatted teacher details

🏫 ClassRoom (Composition)
Attribute	Type
room_number	int
capacity	int

Methods:

__str__() → Returns classroom details

🏢 School (Aggregation + Composition)
Attribute	Type
school_name	str
location	str
students	list
teachers	list
class_room	list
🔧 School Methods
add_students(student)
add_teacher(teacher)
remove_student(student)
remove_teacher(teacher)
add_classroom(room_number, capacity)
display()  # Saves details into Details.txt
💾 File Handling

All school data is saved into:

Details.txt

Each time display() is called, data is appended to the file.

🚀 How to Run

Clone the repository:

git clone https://github.com/your-username/student-management-system.git

Navigate to project folder:

cd student-management-system

Run the script:

python your_script_name.py
🧪 Sample Data Used
Students:

Aasik – AI & ML

Akbar – AI & DS

Anwar – IT

Teachers:

Abdul – Python

Azmar – JAVA

Abdul – ML

Schools:

HISAC (CBE)

HICAS (CBE)
