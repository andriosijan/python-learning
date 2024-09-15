# We all have played snake, water gun game in our childhood. If you haven't, google the rules of this game and write a python program capable of playing this game with the user.

'''
1 = snake
0 = gun
-1 = water
'''
import random
computer = random.choice([1,0,-1])

userInput = input("Enter your choice: ").lower()
userDict = {"s":1, "g":0, "w":-1}
user = userDict[userInput]

reverseDict = {1: "Snake", 0: "Gun", -1: "Water"}
print(f"You choose {reverseDict[user]}\nComputer choose {reverseDict[computer]}")

if(user == computer):
    print("Match is draw")
else:
    if(computer == 1 and user == 0):
        print("You win")
    elif(computer == 1 and user == -1):
        print("You lose!")
    elif(computer == 0 and user == 1):
        print("You lose!")
    elif(computer == 0 and user == -1):
        print("You win")
    elif(computer == -1 and user == 1):
        print("You win")
    elif(computer == -1 and user == 0):
        print("You lose!")
    else:
        print("Something is went wrong")