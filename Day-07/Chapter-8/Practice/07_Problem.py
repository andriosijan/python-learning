# Write a python function to remove a given word from a list ad strip it at the same time

def remove(list,word):
    n = []
    for item in list:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Harry","Rohan","sijan","arafat","an"]

print(remove(l,"an"))