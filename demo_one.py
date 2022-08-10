class Student:
    def __init__(self, university_id, first_name, last_name, year, sem, branch):
        self.university_id = university_id
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.sem = sem
        self.branch = branch

    university_name = 'klh'

    def get_email(self):
        return f'{self.first_name}.{self.last_name}@{Student.university_name}.edu.in'

    @classmethod
    def change_name(cls, new_name):
        cls.university_name = new_name

    @staticmethod
    def static_method():
        print("Welcome to PFSD class")


stu_1 = Student(211003000, 'xyz','abc',2022, 'ODD','CSE')

print("First Name: ",stu_1.first_name)
print("Last Name: ",stu_1.last_name)
print("University Id:",stu_1.university_id)
print("Year: ",stu_1.year)
print("Branch: ",stu_1.branch)

print(stu_1.get_email())
print(stu_1.static_method())

stu_1.change_name('K L University')

print("New name of the university: ",Student.university_name)
