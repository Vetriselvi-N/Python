import random
while True:
    choices=['rock','paper','scissors']
    player=None
    computer=random.choice(choices)
    while player not in choices:
        player=input("rock,paper,scissors?: ").lower()
    if player==computer:
        print("computer= ",computer)
        print("player= ",player)
        print("tie!")
    elif player=="rock":
        if computer=="paper":
            print("computer= ",computer)
            print("player= ",player)
            print("You lose!") 
        if computer=="scissors":
            print("computer= ",computer)
            print("player= ",player)
            print("You win!")
    elif player=="paper":
        if computer=="scissors":
            print("computer= ",computer)
            print("player= ",player)
            print("You lose!")
        if computer=="paper":
            print("computer= ",computer)
            print("player= ",player)
            print("You win!")
    elif player=="scissors":
        if computer=="rock":
            print("computer= ",computer)
            print("player= ",player)
            print("You lose!")
        if computer=="paper":
            print("computer= ",computer)
            print("player= ",player)
            print("You win!")
    play_again=input("play again?(yes/no):").lower()
    if play_again!="yes":
        break
print("Bye!")
