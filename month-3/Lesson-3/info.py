"""
OOP | Inheritance | (Encapsulation, Abstraction, Polymorphism)
Class attributes

Problems:
- RentCar | Base: Vehicle (Car, Bike, Truck)
    - Vehicle: name, seats
        Methods:
            - display_info()
    - Car: name, seats, color, price_per_hour
        Methods:
            - display_info()
            - calculate_price(hours)
            - get_count()
            - rent(from_date, to_date)
    Bike: name, seats, color, price_per_hour
        Methods:
            - display_info()
            - calculate_price(hours)
            - get_count()
            - rent(from_date, to_date)
    Truck: name, seats, color, price_per_hour
        Methods:
            - display_info()
            - calculate_price(hours)
            - get_count()
            - rent(from_date, to_date)


2. Need to crate a program to manage university courses

Classes: Student, Course, Teacher
Student
    Variables:
        name, email, phone_number, id
    Methods:
        - register
        - get_info
        - delete_account
        - get_registered_courses
        - register_to_course

Teacher
    Variables:
        name, phone_number, profession, age
    Methods:
        - add_to_file
        - get_info
        - delete_course
        - get_registered_users

Course
    Variables:
        name, price, teacher
    Methods:
        - add_to_file
        - get_info
        - delete_course
        - get_registered_users

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

