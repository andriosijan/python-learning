# Write a python program using function to convert Celsius to Fahrenheit.

temp = int(input("Enter the temp: "))

def ctof(C):
    return (9/5) * C + 32

print(f"{temp} degree C is euals to: {ctof(temp)} degree F ")