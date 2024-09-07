import random
play=True
num=str(random.randint(10,20))
while play:
    guess=int(input("enter a number betwwen 10 and 20"))
    if num==guess:
        print("you win the game")
    else:
        print("you have lost try again")


    