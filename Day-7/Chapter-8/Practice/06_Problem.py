# Write a python function which converts inches to cms.

inches = int(input("Enter how many inches: "))

def cm_converter(inches):
    cm = inches * 2.54
    return cm

cm = cm_converter(inches)

print(cm ,"centemeter")