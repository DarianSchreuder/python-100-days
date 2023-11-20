import random

num = random.randint(0,1)
choice = int(input("Heads or Tail (0,1): "))
if(num == 0):
    print("Coin landed on: Heads")
else:
    print("Coin landed on: Tails")

if (num == choice):
    print("You Win!")
else:
    print("You Lose!")
    
