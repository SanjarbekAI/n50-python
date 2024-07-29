import json
import os.path


class Student:
    def __init__(self, name, birthday, gender, age):
        self.name = name
        self.birthday = birthday
        self.gender = gender
        self.age = age

    def get_full_info(self):
        return f"Name: {self.name}, Birthday: {self.birthday}"


#
# student1 = Student("John", '09-05-2002', "male", 25)
# print(student1.get_full_info())

# class Operators:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def add(self):
#         return self.num1 + self.num2
#
#     def subtract(self):
#         return self.num1 - self.num2
#
#
# object1 = Operators(12, 9)
# object2 = Operators(100, 10)
# object3 = Operators(123, 13)
# import os
#
#
# class JsonManager:
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def check_existence(self):
#         if os.path.exists(self.file_name):
#             return True
#         return False
#
#     def create_json_file(self):
#         if not self.check_existence():
#             with open(self.file_name, 'x'):
#                 return "File is created"
#         return "FIle exists"
#
#     def read_json_file(self):
#         if self.check_existence():
#             if os.path.getsize(self.file_name) != 0:
#                 with open(self.file_name, 'r') as file:
#                     return json.load(file)
#             return []
#         return []
#
#     def write_json_file(self, all_data):
#         if self.check_existence():
#             with open(self.file_name, mode='w') as file:
#                 json.dump(all_data, file, indent=4)
#                 return "Data is added"
#         return "File does not exist"
#
#     def add_one_data(self, data: dict):
#         if self.check_existence():
#             all_data = self.read_json_file()
#             all_data.append(data)
#             return self.write_json_file(all_data)
#         return "File does not exist"
#
#     def add_more_data(self, data: list):
#         if self.check_existence():
#             all_data = self.read_json_file()
#             for user in data:
#                 all_data.append(user)
#             return self.write_json_file(all_data)
#         return "File does not exist"
# import csv
#
#
# class CSVFileManager:
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def create_file(self):
#         with open(self.file_name, 'x'):
#             return "File is created"
#
#     def check_file(self):
#         if os.path.exists(self.file_name):
#             return True
#         return False
#
#     def write_headers(self, headers: str):
#         if self.check_file():
#             with open(self.file_name, 'w') as file:
#                 file.write(headers)
#                 return "Headers written"
#         return "File does not exist"
#
#     def write_file(self, data: str):
#         with open(self.file_name, 'a') as file:
#             file.write("\n" + data)
#             return "Data written"
#
#     def read_file(self):
#         if self.check_file():
#             with open(self.file_name, mode='r') as file:
#                 return csv.reader(file)
#         return "File does not exist"
#
#     def delete_file(self):
#         if self.check_file():
#             os.remove(self.file_name)
#             return "File is deleted"
#         return "File does not exist"
#
#     def clear_file(self):
#         if self.check_file():
#             with open(self.file_name, mode='r') as file:
#                 for row in csv.reader(file):
#                     self.write_headers(f"{row[0]},{row[1]},{row[2]}")
#                     return "File is cleaned"
#         return "File does not exist"
#
#
# csv_file = CSVFileManager("new.csv")
# # csv_file.create_file()
# # csv_file.write_headers("Name,Birthday,Gender")
# # csv_file.write_file("Sanjarbek,2002-09-05,male")
# # print(csv_file.read_file())
# csv_file.clear_file()
