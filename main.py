from models import Student, StudentManager
from utils import (
    display_menu,
    get_non_empty_string,
    get_positive_int,
    get_year,
    get_email,
    get_phone,
)


def add_student_flow(manager):
    print("\n--- Add Student ---")
    try:
        student_id = get_non_empty_string("Enter Student ID: ")
        name = get_non_empty_string("Enter Name: ")
        branch = get_non_empty_string("Enter Branch (e.g., CSE, ECE): ")
        year = get_year()
        email = get_email()
        phone = get_phone()

        student = Student(student_id, name, branch, year, email, phone)
        manager.add_student(student)
        print("Student added successfully!")
    except ValueError as e:
        print(f"Error: {e}")


def view_all_students(manager):
    print("\n--- All Students ---")
    students = manager.view_all_students()
    if not students:
        print("No students found.")
        return
    for s in students:
        print(s)


def search_by_id_flow(manager):
    print("\n--- Search Student by ID ---")
    student_id = get_non_empty_string("Enter Student ID: ")
    student = manager.search_by_id(student_id)
    if student:
        print("Student found:")
        print(student)
    else:
        print("No student found with this ID.")


def search_by_name_flow(manager):
    print("\n--- Search Student by Name ---")
    name_part = get_non_empty_string("Enter name (or part of name): ")
    results = manager.search_by_name(name_part)
    if not results:
        print("No students found matching this name.")
    else:
        print(f"Found {len(results)} student(s):")
        for s in results:
            print(s)


def update_student_flow(manager):
    print("\n--- Update Student ---")
    student_id = get_non_empty_string("Enter Student ID to update: ")
    try:
        student = manager.search_by_id(student_id)
        if not student:
            print("No student found with this ID.")
            return

        print(f"Current details: {student}")
        print("Press Enter to keep existing value.")

        name = input(f"Name [{student.name}]: ").strip()
        branch = input(f"Branch [{student.branch}]: ").strip()
        year_str = input(f"Year [{student.year}]: ").strip()
        email = input(f"Email [{student.email}]: ").strip()
        phone = input(f"Phone [{student.phone}]: ").strip()

        updates = {}
        if name:
            updates["name"] = name
        if branch:
            updates["branch"] = branch
        if year_str:
            updates["year"] = int(year_str)
        if email:
            updates["email"] = email
        if phone:
            updates["phone"] = phone

        updated = manager.update_student(student_id, **updates)
        print("Student updated successfully!")
        print(updated)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def delete_student_flow(manager):
    print("\n--- Delete Student ---")
    student_id = get_non_empty_string("Enter Student ID to delete: ")
    confirm = input(f"Are you sure you want to delete student ID {student_id}? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Deletion cancelled.")
        return
    try:
        deleted = manager.delete_student(student_id)
        print("Student deleted successfully!")
        print(f"Deleted: {deleted}")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    manager = StudentManager()

    while True:
        display_menu()
        choice = input("Enter your choice (1–7): ").strip()

        if choice == "1":
            add_student_flow(manager)
        elif choice == "2":
            view_all_students(manager)
        elif choice == "3":
            search_by_id_flow(manager)
        elif choice == "4":
            search_by_name_flow(manager)
        elif choice == "5":
            update_student_flow(manager)
        elif choice == "6":
            delete_student_flow(manager)
        elif choice == "7":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
