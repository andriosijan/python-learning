# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

def game():
    f = open("highscore.txt","r")
    high_score = f.read()
    f.close()

    score = int(input("What is your score: "))

    if(len(high_score) >= 1):
        high_score = int(high_score)

        if (score > high_score):
            print(f"The new high score is: {score}")
            f = open("highscore.txt","w")
            f.write(str(score)) 
            f.close()  
        else:
            print(f"The high score is: {high_score}")    
    else:
        print(f"The new high score is: {score}")
        f = open("highscore.txt","w")
        f.write(str(score)) 
        f.close()



game()    