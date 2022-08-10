class Employee:
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    company = 'Youtube'

    def get_email(self):
        return f'{self.first_name}.{self.last_name}@{Employee.company}com'


emp1 = Employee('John', 'Smith')
print(emp1.get_email())
print(emp1.last_name)