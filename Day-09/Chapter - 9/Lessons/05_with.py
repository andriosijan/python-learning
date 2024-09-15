f = open("01_files.txt")
print(f.read())
f.close()


#The same can be writter using with statement like this:
with open("01_files.txt") as f:
    print(f.read())

# You don't have to explicitly close the file