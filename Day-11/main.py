############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import os
import art
import random
print(art.logo)

bank_balance = 1000
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pick_card():
    return cards[random.randint(0,12)]

def calcTotal(list:list):
    return sum(list)
def win(bank_balance,gamble_amount):
    bank_balance += gamble_amount
    print(f"win = {gamble_amount}")
    return bank_balance
    
def display(player_list:list, computer_list:list, bank_balance, gamble_amount):
    os.system('clear')
    print(f"Players Cards:\n{player_list}\nPlayer Total: {calcTotal(player_list)}")
    if (sum(computer_list) < 3):
        print(f"Computers Cards:\n{computer_list[0]},HIDDEN\nComputer Total: {computer_list[0]}")
    else:
        index = len(computer_list)
        list = computer_list.copy()
        list.pop(index-1)
        print(f"Computers Cards:\n{list},HIDDEN\nComputer Total: {calcTotal(list)}\nBank Balance: {bank_balance}")
    
def bust(player_list:list, computer_list:list,bank_balance,gamble_amount):
    if(sum(player_list) == sum(computer_list)):
        print(f"Draw!\nPlayer: {sum(player_list)} | Computer: {sum(computer_list)}")
        return win(gamble_amount, bank_balance)
    elif(sum(player_list) > 21):
        print(f"Computer Wins!\nPlayer: {sum(player_list)} | Computer: {sum(computer_list)}")
        return bank_balance
    else:
        print(f"Player Wins!\nPlayer: {sum(player_list)} | Computer: {sum(computer_list)}")
        return win(gamble_amount*2,bank_balance)
        
def hit(list:list):
    card = pick_card()
    if card == 11:
        if (sum(list) + card) > 21:
            list.append(1)
    else:
        list.append(card)
            
    
def checkWin(player_list:list, computer_list:list,bank_balance,gamble_amount):
    player_total = sum(player_list)
    computer_total = sum(computer_list)
    
    if (player_total > 21 or computer_total > 21):
        return bust(player_list, computer_list,bank_balance,gamble_amount)
    elif (player_total == computer_total):
        print(f"Draw!\nPlayer: {player_total} | Computer: {computer_total}")
        return win(gamble_amount, bank_balance)
    elif(player_total > computer_total and player_total <= 21):
        print(f"Player Wins!\nPlayer: {player_total} | Computer: {computer_total}")
        return win(gamble_amount*2, bank_balance)
    elif(computer_total>player_total and computer_total <= 21):
        print(f"Computer Wins!\nPlayer: {player_total} | Computer: {computer_total}")
        return bank_balance


    
def deal(bank_balance,gamble_amount):
    player_cards = []
    computer_cards = []
    for i in range(0, 2):
        player_cards.append(pick_card())
        computer_cards.append(pick_card())
    done = False
    while not done:   
        display(player_cards,computer_cards,bank_balance,gamble_amount)
        total = 0
        for i in range(0,len(computer_cards) - 1):
            total += computer_cards[i]
        if(sum(player_cards) > 21 or sum(computer_cards) > 21):
            bank_balance = bust(player_cards,computer_cards,bank_balance,gamble_amount)
            return bank_balance
        else:
            if(input("Hit or Stand?: ") == "hit"):
                hit(player_cards)
                if sum(computer_cards) < 17:
                    hit(computer_cards)
            elif sum(computer_cards) < 17:
                hit(computer_cards) 
            else:
                bank_balance = checkWin(player_cards,computer_cards,bank_balance,gamble_amount)
                return bank_balance
            
    
        
    

while bank_balance > 0:
    gamble_amount = int(input("How much would you like to gamble? (All in?: -1): "))
    
    if (gamble_amount == -1):
        print("All IN!")
        gamble_amount = bank_balance
        bank_balance = 0
        bank_balance = deal(bank_balance,gamble_amount)
    elif(gamble_amount > 0 and gamble_amount <= bank_balance):
        print(f"Playing with {gamble_amount}")
        bank_balance -= gamble_amount
        bank_balance = deal(bank_balance,gamble_amount)
    else: 
        os.system('clear')
        print("invalid amount.")
        
        
    
    









































##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

