# Write a program to print multiplication table of a given number using while loop.

num = int(input("Enter a number: "))

i = 1
while(i<=10):
    print(f"{num} X {i} = {i*num}")
    i += 1