#Encapsulation - is the process of wrapping data and methods into a single unit (class) and restricting direct access to some of the data.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # Private variable

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if new_marks >= 0:
            self.__marks = new_marks
        else:
            print("Marks cannot be negative!")

s1 = Student("Ken", 85)

print(s1.get_marks())   # 85
s1.set_marks(-50)       # Not allowed
