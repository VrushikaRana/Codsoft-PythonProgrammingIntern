# Rock Paper Scissors Game 

import random

print("Welcome to ROCK, PAPER, SCISSORS GAME")
print("\n")
print("Winning Rules are as under : \nRock Vs Scissors hence Rock Wins \nPaper Vs Rock hence Paper Wins \nScissors Vs Paper hence Scissors Wins ")
print("\n")
list_=["Rock","Paper","Scissors"]
user=input("Choose one : 'Rock','Paper','Scissors' ")
print("Choice you chosen : ",user)
computer=random.choice(list_)
print("Random choice by computer : ",computer)

if user=="Rock" and computer=="Scissors": 
    print("Congratulations.....You Won !!!")
elif user=="Paper" and computer=="Rock": 
    print("Congratulations.....You Won !!!")
elif user=="Scissors" and computer=="Paper": 
    print("Congratulations.....You Won !!!")
elif user==computer:
    print("It's a DRAW...!!!")
else:
    print("You LOST.....")   
