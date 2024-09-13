# Write a recursive function to calculate the sum of first n natural numbers.

n = int(input("Enter the value of n: "))
def count_numbers(n):
    if(n<=1):
        return 1
    return n + count_numbers(n-1)

print(f"The sum of first {n} natural numbers are: {count_numbers(n)}")
