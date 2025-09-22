def add_student(students):
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    students[name] = grade
    print(f"✅ Added {name} with grade {grade}")


def view_students(students):
    if not students:
        print("No students yet.")
        return
    print("\n📚 Students:")
    for name, grade in students.items():
        print(f"{name}: {grade}")


def run_sms():
    students = {}
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    run_sms()
