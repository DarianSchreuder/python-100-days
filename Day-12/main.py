logo = """

  _______  __    __   _______     _______.     _______. __  .__   __.   _______      _______      ___      .___  ___.  _______ 
 /  _____||  |  |  | |   ____|   /       |    /       ||  | |  \ |  |  /  _____|    /  _____|    /   \     |   \/   | |   ____|
|  |  __  |  |  |  | |  |__     |   (----`   |   (----`|  | |   \|  | |  |  __     |  |  __     /  ^  \    |  \  /  | |  |__   
|  | |_ | |  |  |  | |   __|     \   \        \   \    |  | |  . `  | |  | |_ |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
|  |__| | |  `--'  | |  |____.----)   |   .----)   |   |  | |  |\   | |  |__| |    |  |__| |  /  _____  \  |  |  |  | |  |____ 
 \______|  \______/  |_______|_______/    |_______/    |__| |__| \__|  \______|     \______| /__/     \__\ |__|  |__| |_______|
                                                                                                                               

"""
import random
NUMBER = random.randint(1,100)
GUESSED = False
def guessing_game():
    print("Welcome to the number guessing game")
    print("Im thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type \"easy\" or \"hard\"")
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    else:
        print("invalid")
    global NUMBER, GUESSED
    
    while lives > 0 and  GUESSED == False:
        print(f"You have {lives} attempts remaining.")
        guess = int(input("Make a guess: "))
        if guess <= 100 or guess >= 1:
            if guess == NUMBER:
                print(f"You got it the answer was {NUMBER}")
                GUESSED = True
            elif guess > NUMBER:
                print("Too High")
            elif guess < NUMBER:
                print("Too Low")
            lives -= 1
        else:
            print(f"Invalid number {guess}")
        print("Guess Again")
    

guessing_game()