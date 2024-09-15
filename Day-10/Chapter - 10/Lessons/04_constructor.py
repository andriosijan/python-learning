class Employee:
    language = "Python" #This is a class attribute
    salary = 120000

    def __init__(self,name,salary,language): # Dunder mathod which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


    @staticmethod # It means this do not take argument
    def greet():
        print("Good morning")    

harry = Employee("Sijan",1500000,"JavaScript")
print(harry.name, harry.salary,harry.language)
harry.getInfo()

