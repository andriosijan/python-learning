# Write a program to mine a log file and find out whether it contains 'pyton'.

with open("log.txt", 'r') as f:
    content = f.read()

if("python" in content):
    print("Yes, python is available in the file")
else:
    print("No, python is not available in the file")