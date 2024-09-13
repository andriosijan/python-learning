# Write a python function to print multiplication table of a given number.

num = int(input("Enter the number: "))

def mul(num):
    i = 1
    while(i <= 10):
        print(f"{num} X {i} = {num*i}")
        i +=1
mul(num)