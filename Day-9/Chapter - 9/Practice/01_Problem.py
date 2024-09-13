# write a program to read the text from a given file "poems.txt" and find out whether it contains the word "twinkle"
f = open("poems.txt")
poem = f.read()
if(poem.lower().find("twinkle")!= -1):
    print("Yes, twinkle is available in the poem")
else:
    print("No! twinkle is not available in the poem")

f.close()