import random
def game():
    print("you are playing the game")
    score=random.randint(1,62)
    with open("history.txt") as f:
        history=f.read()
        if(history!=""):
            history=int(history)
        else:
            history=0
    print(f"u r score: {score}")
    if(score>history):
        with open("history.txt","w") as f:
            f.write(str(score))
    return score
game()