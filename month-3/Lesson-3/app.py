# class Employee:
#     salary_growth = 4
#
#     def __init__(self, full_name, salary):
#         self.full_name = full_name
#         self.salary = salary
#
#     def display_info(self):
#         return f"{self.full_name} {self.salary}"
#
#     def increase_salary(self):
#         self.salary += (self.salary * self.salary_growth / 100)
#         return self.salary
#
#
# class Developer(Employee):
#     salary_growth = 5
#
#     def __init__(self, full_name, salary, prog_lang):
#         super().__init__(full_name, salary)
#         self.prog_lang = prog_lang
#
#     def display_info(self):
#         return f"{super().display_info()}, {self.prog_lang}"
#
#
# class Teacher(Employee):
#     def __init__(self, full_name, salary, profession):
#         super().__init__(full_name, salary)
#         self.profession = profession
#
#
#
#
#
# dev1 = Developer("Sanjarbek", 2000, "Python")
# print(dev1.display_info())
#
# print(help(Developer))
#
# emp1 = Employee("Sanjar", 2000)
#
# emp1.increase_salary()
# print(emp1.display_info())


class Teacher:
    file_name = "teachers.txt"

    def read_data(self):
        with open(self.file_name, 'r') as file:
            data = file.readlines()
            return data

    def get_info(self, phone_number):
        data = self.read_data()
        for row in data:
            teacher = row.split(",")
            if teacher[1] == phone_number:
                return "Teacher is " + teacher[0]
        return "No teacher found"

    def add_to_file(self, full_name, phone_number, profession, age):
        with open(self.file_name, 'w') as file:
            file.write(f"{full_name},{phone_number},{profession},{age}\n")
            return "Added"

    def find_teacher(self, phone_number):
        data = self.read_data()
        for row in data:
            teacher = row.split(",")
            if teacher[1] == phone_number:
                return teacher
        return "No teacher found"


class Course:
    file_name = "courses.txt"

    def add_to_file(self, course_name, price, teacher_name):
        with open(self.file_name, 'w') as file:
            file.write(f"{course_name},{price},{teacher_name},\n")
            return "Added"


def show_menu():
    print("Welcome to menu: ")
    user_input = int(input("What would you like to"))
    teacher = Teacher()
    courses = Course()

    if user_input == 1:
        full_name = input("What is your full: ")
        phone_number = input("Phone: ")
        profession = input("Profession: ")
        age = input("Age: ")
        result = teacher.add_to_file(full_name, phone_number, profession, age)
        print(result)
    elif user_input == 2:
        course_name = input('Enter the course name: ')
        price = input('Enter the price: ')
        teacher_phone_number = input('Enter teacher\'s phone number')
        teacher_info = teacher.find_teacher(teacher_phone_number)
        result = courses.add_to_file(course_name, price, teacher_info)
        print(result)


show_menu()

courses = [
    {
        "name": "Python",
        "price": 12000,
        "teacher": {
            "full_name": "sasa",
            "phone_number": "saca",
            "profession": "prfadsc",
            "age": 22
        }
    },
    {
        "name": "Python",
        "price": 12000,
        "teacher": {
            "full_name": "sasa",
            "phone_number": "saca",
            "profession": "prfadsc",
            "age": 22
        }
    },
    {
        "name": "Python",
        "price": 12000,
        "teacher": {
            "full_name": "sasa",
            "phone_number": "saca",
            "profession": "prfadsc",
            "age": 22
        }
    }
]
