class Employee:
    language = "py" #this is a class attribute
    salary = 12000000

harry = Employee()
harry.name = "Harry" #This is an instance attribute
print(harry.name, harry.language,harry.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name,rohan.language,rohan.salary)

# Here name is instance attribute and salary and language attribute as they directly belong to the class