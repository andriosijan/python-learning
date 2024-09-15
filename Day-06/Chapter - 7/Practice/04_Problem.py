# Write a program to find whether a given number is prime or not.

i = 2
num = int(input("Enter a number: "))

if(num>=2):
    while(i<num):
        if(num%i==0):
            print("The number is not a prime number")
            break
        i +=1    
    else:
        print("The number is a prime number")          
else:
    print("The number is not a prime number")
  
    