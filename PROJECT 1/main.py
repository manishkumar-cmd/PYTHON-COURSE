# import random
# computer=random.choice([1,-1,0])
# youstr=input("enter your choice")
# youdict={"s":1,"w":-1,"g":0}
# reversedict={1:"snake",-1:"water",0:"gun"}
# you=youstr[youdict]
# print(f"you chose{reversedict[you]}\ncomputer chose {reversedict[computer]}")
# if(computer==you):
#     print("its a draw")
# else:
#     if(computer==-1 and you==1):
#         print("you winnn")
#     elif(computer==-1 and you ==1):
#         print("you lose")
#     if(computer==1 and you==-1):
#         print("you lose")
#     elif(computer==1 and you ==0):
#         print("you winnn")
#     if(computer==0 and you==-1):
#         print("you winnn")
#     elif(computer==0 and you ==1):
#         print("you lose")
#     else:
#         print("something went wrong")
        
        
        
        
import random
computer = random.choice([1, -1, 0])
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "snake", -1: "water", 0: "gun"}
if youstr not in youdict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    you = youdict[youstr]
    print(f"You chose {reversedict[you]}")
    print(f"Computer chose {reversedict[computer]}")
    if computer == you:
        print("It's a draw!")
    elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
        print("You win!")
    else:
        print("You lose!")
        
        
        
        
        
        
print(f"you chose{reversedict}")