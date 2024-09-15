# Create a Class "Programmer" for stoting information of few programmers working in Microsoft

class Programmer:
    company = "Microsoft"

    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary

harry = Programmer("Harry","python",10000)
rohan = Programmer("Rohan","java",50000)
sijan = Programmer("Sijan","JavaScript",15000)

print(harry.name,harry.company,harry.language,harry.salary)
print(sijan.name,sijan.company,sijan.language,sijan.salary)
print(rohan.name,rohan.company,rohan.language,rohan.salary)
