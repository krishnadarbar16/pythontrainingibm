# Number Guessing Game
# Generate a random number and let the user guess it.
# Use conditionals to give hints ("Too high", "Too low").
import random 
# import numpy as np
# a=np.array([1,2,3,4])
# print(a)
num= random.randint(1,100)
user = int(input("guess the num:"))
count=0
while True:
    count+=1
    if(num<user):
        print("too high")
        user = int(input("try again:"))
        if(count==5):
            print("you lost your 5 attempts ")
            break
    elif(num>user):
        print("too low")
        user = int(input("try again:"))
        if(count==5):
            print("you lost your 5 attempts ")
            break
    elif(num==user):
        print(f"you guessed {num} correct .....YOU WIN.......")
        break
print(".....GAME ENDED......")