import json
import os

DATA_FILE = "data/students.json"


class Student:
    def __init__(self, student_id, name, branch, year, email, phone):
        self._student_id = student_id
        self._name = name
        self._branch = branch
        self._year = year
        self._email = email
        self._phone = phone

    @property
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def branch(self):
        return self._branch

    @branch.setter
    def branch(self, value):
        self._branch = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    def to_dict(self):
        return {
            "student_id": self._student_id,
            "name": self._name,
            "branch": self._branch,
            "year": self._year,
            "email": self._email,
            "phone": self._phone,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["name"],
            data["branch"],
            data["year"],
            data["email"],
            data["phone"],
        )

    def __str__(self):
        return (
            f"ID: {self._student_id} | Name: {self._name} | Branch: {self._branch} "
            f"| Year: {self._year} | Email: {self._email} | Phone: {self._phone}"
        )


class StudentManager:
    def __init__(self):
        self.students = []
        self._load_data()

    def _ensure_data_dir(self):
        os.makedirs("data", exist_ok=True)

    def _load_data(self):
        self._ensure_data_dir()
        if not os.path.exists(DATA_FILE):
            self.students = []
            return
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.students = [Student.from_dict(s) for s in data]
        except (json.JSONDecodeError, KeyError):
            self.students = []

    def _save_data(self):
        self._ensure_data_dir()
        data = [s.to_dict() for s in self.students]
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def add_student(self, student):
        for s in self.students:
            if s.student_id == student.student_id:
                raise ValueError("Student ID already exists.")
        self.students.append(student)
        self._save_data()

    def view_all_students(self):
        return self.students

    def search_by_id(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def search_by_name(self, name_part):
        name_part = name_part.lower()
        return [s for s in self.students if name_part in s.name.lower()]

    def update_student(self, student_id, **updates):
        student = self.search_by_id(student_id)
        if not student:
            raise ValueError("Student not found.")
        if "name" in updates:
            student.name = updates["name"]
        if "branch" in updates:
            student.branch = updates["branch"]
        if "year" in updates:
            student.year = updates["year"]
        if "email" in updates:
            student.email = updates["email"]
        if "phone" in updates:
            student.phone = updates["phone"]
        self._save_data()
        return student

    def delete_student(self, student_id):
        student = self.search_by_id(student_id)
        if not student:
            raise ValueError("Student not found.")
        self.students = [s for s in self.students if s.student_id != student_id]
        self._save_data()
        return student
