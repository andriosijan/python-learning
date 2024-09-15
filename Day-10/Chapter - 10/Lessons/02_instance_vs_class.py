class Employee:
    language = "Python" #This is a class attribute
    salary = 120000

harry = Employee()
harry.language = "Javascript" #This is an instance attribute
print(harry.language, harry.salary)