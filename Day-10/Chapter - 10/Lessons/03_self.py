class Employee:
    language = "Python" #This is a class attribute
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


    @staticmethod # It means this do not take argument
    def greet():
        print("Good morning")    

harry = Employee()
# harry.language = "Javascript" #This is an instance attribute
harry.greet()
harry.getInfo()
# Employee.getInfo(harry)
