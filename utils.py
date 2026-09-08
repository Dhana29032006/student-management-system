def display_menu():
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Search Student by Name")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. Exit")
    print("=================================")


def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def get_positive_int(prompt):
    while True:
        value = input(prompt).strip()
        try:
            num = int(value)
            if num > 0:
                return num
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_year():
    while True:
        value = input("Enter year (1–4): ").strip()
        try:
            year = int(value)
            if 1 <= year <= 4:
                return year
            else:
                print("Year must be between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_email():
    while True:
        email = input("Enter email: ").strip()
        if "@" in email and "." in email:
            return email
        print("Please enter a valid email (e.g., name@example.com).")


def get_phone():
    while True:
        phone = input("Enter phone number (digits only): ").strip()
        if phone.isdigit() and len(phone) >= 10:
            return phone
        print("Please enter a valid phone number (at least 10 digits).")
