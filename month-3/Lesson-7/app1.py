class Student:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return self.full_name


class StudyCenter:
    def __init__(self, name, year, location):
        self.name = name
        self.location = location
        self.year = year
        self.students = []

    def __getitem__(self, item):
        return self.students[item]

    def __setitem__(self, key, value):
        self.students[key] = value

    def __str__(self):
        return "salom"

    def __repr__(self):
        return f"StudyCenter(name={self.name}, year={self.year}, location={self.location})"

    def another(self):
        return "Abubakr"

    def __call__(self, *args, **kwargs):
        if args:
            for arg in args:
                if isinstance(arg, Student):
                    self.students.append(arg)

    def __len__(self):
        return len(self.students)

    def __add__(self, other):
        return self.year + other.year

    def __sub__(self, other):
        return self.year - other.year

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass


nt = StudyCenter(name="Najot  Talim", year=2020, location="tashkent")
pdp = StudyCenter(name="Najot  Talim", year=2020, location="tashkent")

st1 = Student(full_name="Sanjarbek", age=34)
st2 = Student(full_name="Sardor", age=34)
nt(st1)

nt[0] = st2
print(nt[0])

# new_nt = str(nt)
# print(new_nt)

# print(nt.__len__())
# print(nt.__dir__())
#



# print(nt())
# new_nt = nt.__dict__
# print(nt.__repr__())
