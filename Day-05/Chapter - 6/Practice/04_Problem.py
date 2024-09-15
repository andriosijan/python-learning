# Write a program to find whether a given username contains less then 10 characters or not?

username = input("Enter you username: ")

if(len(username)<10):
    print("This username contains less then 10 characters")
else:
    print("This username constains more then 10 characters")