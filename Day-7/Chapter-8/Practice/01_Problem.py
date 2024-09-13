# Write a program using function to find greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b    
    else:
        return c    
    


print("The greatest number is: ",greatest(5,50,6))