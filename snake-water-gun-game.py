#SNAKE , WATER AND GUN GAME
import random
def game(user):
    l=["snake","water","gun"]
    r=random.choice(l)
    if ((r.lower()==user.lower())):
        print("It's a Draw !,since the computer choose:",r)
    elif ((r.lower()=="snake") and (user.lower()=="water")):
        print("Computer wins !,since the computer choose:",r)
    elif ((r.lower()=="water") and (user.lower()=="gun")):
        print("Computer wins !since the computer choose:",r)
    elif((r.lower()=="gun") and (user.lower()=="snake")):
        print("Computer wins !,since the computer choose:",r)
    elif ((user.lower()=="snake") and (r.lower()=="water")):
        print("Congratulations You Win !,since the computer choose:",r)
    elif ((user.lower()=="water") and (r.lower()=="gun")):
        print("Congratulations You Win !,since the computer choose:",r)
    elif((user.lower()=="gun") and (r.lower()=="snake")):
        print("Congratulations You Win, since the computer choose:",r)
    else:
        print("Wrong input ! Try again !")

print("WELCOME TO SNAKE,WATER,GUN GAME")
x=input("Enter your choice Snake, Water ,Gun: ")
game(x)

