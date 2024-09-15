# Write a program to calculate the grade of a student from his marks from the following scheme:
'''
90-100 => Ex
80-90 => A
70-80 => B
60-70 => C
50-60 => D
<50 => F
'''

marks = int(input("Enter your marks: "))

if(marks >= 90):
    print("Congrats, you have got: Ex.")
elif(marks>=80 and marks<90):
    print("Congrats, you have got: A")
elif(marks>=70 and marks<80):
    print("Congrats, you have got: B")
elif(marks>=60 and marks<70):
    print("Congrats, you have got: C")
elif(marks>=50 and marks<60):
    print("Congrats, you have got: D")
elif(marks<50):
    print("You are failed")
