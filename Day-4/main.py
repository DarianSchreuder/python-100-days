import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
list = [rock, paper, scissors]
computer = random.randint(0,2)
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("Computer: \n"+list[computer]+"\nPlayer: \n" + list[choice])
if (computer == choice):
    print("Draw")
else:
    if((choice == 0 and computer == 1) or (computer == 0 and choice == 2) or (choice == 1 and computer == 2)):
        print("Computer Wins.")
    else:
        print("Player Wins.")