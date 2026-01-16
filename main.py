from db import SessionLocal, Student

session = SessionLocal()

def add_student(name, age, course):
    student = Student(name=name, age=age, course=course)
    session.add(student)
    session.commit()
    print("Student added successfully")

def view_students():
    students = session.query(Student).all()
    for s in students:
        print(f"ID: {s.id}, Name: {s.name}, Age: {s.age}, Course: {s.course}")

if __name__ == "__main__":
    add_student("Shruti", 21, "Computer Science")
    view_students()
