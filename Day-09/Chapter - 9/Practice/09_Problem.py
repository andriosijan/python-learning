# Write a program to find out whether a file is identical and matches the content of another file.

with open("this.txt", 'r') as f:
    data_1 = f.read()

with open("this_copy.txt", 'r') as f:
    data_2 = f.read()   

if(data_1 == data_2):
    print("yes, this 2 files are identical") 

else:
    print("No, this 2 files are not identical")    