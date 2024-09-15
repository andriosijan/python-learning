# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subjest to pass. Assume 3 subjects and take marks as an input from the user.
bangla = int(input("Enter your marks in bangla: "))
english = int(input("Enter your marks in english: "))
math = int(input("Enter your marks in math: "))

total_percentage = (bangla+english+math)/(300/100)
if(total_percentage>=40 and bangla>=33 and english>=33 and math>=33):
    print("congrats, you are passed: ",total_percentage)
else:
    print("Sorry, you are failed: ",total_percentage)