# Write a program which finds out whether a given name is present in a list or not.

ls = ['rohan','shobam','sijan','arafat']
name = input("Enter you name: ")

if(name in ls):
    print(f"Yes, {name} is available in the list")
else:
    print(f"No, {name} is not available in the list ")