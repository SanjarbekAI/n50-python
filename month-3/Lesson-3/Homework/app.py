menu = """
Menu:
    1. Create a new teacher: name, phone_number, profession, age
    2. Crate a course: name, price, teacher_phone_number
    3. Register to course: name, email, phone_number, id
    4: Delete a course: name
    5: Delete a teacher: phone_number
    6: Get registered courses: phone_number
    7. Get users by course: course_name
    8. Exit
"""

"""
JsonManager() -> class variable -> teachers.json, courses.json, students.json
Student() -> name, phone_number
Teacher() -> name, phone_number, experience, profession
Course() -> name, price, teacher(object)
"""

students = [
    {
        "name": "<NAME>",
        "phone_number": "phone_number"
    },
    {
        "name": "<NAME>",
        "phone_number": "phone_number"
    }
]

teachers = [
    {
        "name": "<NAME>",
        "phone_number": "phone_number",
        "experience": "experience",
        "profession": "profession",
    },
    {
        "name": "<NAME>",
        "phone_number": "phone_number",
        "experience": "experience",
        "profession": "profession",
    }
]

courses = [
    {
        "name": "Course",
        "price": "12131",
        "teacher": {
            "name": "<NAME>",
            "phone_number": "phone_number",
            "experience": "experience",
            "profession": "profession",
        }
    },
    {
        "name": "Course",
        "price": "12131",
        "teacher": {
            "name": "<NAME>",
            "phone_number": "phone_number",
            "experience": "experience",
            "profession": "profession",
        }
    }
]
import json, os


class JsonManager:
    def __init__(self):
        self.teachers_file = './files/teachers.json'
        self.students_file = './files/students.json'
        self.courses_file = './files/courses.json'

    def select_file(self, file_name):
        if 'teachers' in file_name:
            return self.teachers_file
        elif 'students' in file_name:
            return self.students_file
        elif 'courses' in file_name:
            return self.courses_file
        return file_name

    def read_data(self, file_name):
        file_name = self.select_file(file_name)
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            with open(file_name, 'w') as file:
                json.dump([], file, indent=4)
                return []
        except json.decoder.JSONDecodeError:
            if os.path.getsize(file_name) == 0:
                return []

    def write_data(self, file_name, data: dict):
        file_name = self.select_file(file_name)
        with open(file_name, 'w') as file:
            all_data = self.read_data(file_name)
            all_data.append(data)
            json.dump(all_data, file, indent=4)
            return "Data written to file"


class People:
    def __init__(self, name, phone_numer):
        self.name = name
        self.phone_numer = phone_numer


class Teacher(People):
    def __init__(self, name, phone_numer, experience, profession):
        super().__init__(name, phone_numer)
        self.experience = experience
        self.profession = profession

    def change_to_dict(self):
        return {
            'name': self.name,
            'phone_numer': self.phone_numer,
            'experience': self.experience,
            'profession': self.profession
        }


class Student(People):
    def __init__(self, name, phone_numer, age):
        super().__init__(name, phone_numer)
        self.age = age


file_manager = JsonManager()


def get_teacher_info():
    name = input('Enter your name: ')
    phone_numer = input('Enter your phone: ')
    experience = input('Enter your experience: ')
    profession = input('Enter your profession: ')

    teacher = Teacher(name, phone_numer, experience, profession)
    file_manager.write_data(file_name='teachers.json', data=teacher.change_to_dict())
    print(f"Teacher's name: {teacher.name} is added")
    return show_menu()


def show_menu():
    print(menu)
    user_input = int(input("Enter your choice: "))

    if user_input == 1:
        get_teacher_info()


if __name__ == '__main__':
    show_menu()
