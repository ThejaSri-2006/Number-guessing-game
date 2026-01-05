#Number guessing game

import random
print("Welcome to the game")
lowerbound = int(input("Enter the starting limit:"))
upperbound = int(input("Enter the ending point:"))
print("You have only 7 chances")
num = random.randint(lowerbound,upperbound)
chance = 7
count = 0
while count < chance :
    count += 1
    number = int(input("enter a number:"))
    if number == num:
        print("Exact Answer")
    elif number < num:
        print("Too low")
    elif number > num:
        print("Too long")
    elif count > chance and number != num:
        print("sorry, you have lot")

    
