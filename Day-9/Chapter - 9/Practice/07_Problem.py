# Write a program to find out the line number where python is present from question no 6 .

with open("log.txt") as f:
    data = f.read()
    
    
if("python" in data):
    
    with open("log.txt") as f:
        find = False
        line = 1

        while(find == False):
            data = f.readline()
            if("python" in data):
                find = True
                print(f"Python is in line number: {line}")
            line += 1    
else:
    print("Python is not present in the file")        