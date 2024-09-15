# Create a class with attribute a; create an object from it and set "a" directly using object.a = 0, does this change the class attribute?

class Demo:
    a = 1


num = Demo()
print(num.a) # Print the class attribute because instance attribute is not present
num.a = 0 # Instance attribute is set
print(num.a) # Prints the instance attribute because instance attribute is present
print(Demo().a)

# No it does not changes the class attribute😎✌