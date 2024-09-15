# Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter a number: "))

for i in range(10):
    print(f"{n} X {10-i} = {n * (10-i)}")
