from abc import ABC, abstractmethod

class ImplementationError(Exception):
    pass

class People(ABC):
    def __init__(self):
        if 'introduce' not in self.__class__.__dict__:
            raise ImplementationError("hello")

    @abstractmethod
    def introduce(self):
        raise NotImplementedError("Please implement this method")

class Student(People):
    def introduce2(self):
        return "Hello, I am a student"

# Uncomment the following lines to test the behavior
# This will raise the ImplementationError with the message "hello"
try:
    p1 = Student()
except ImplementationError as e:
    print(f"Custom Error Message: {e}")
