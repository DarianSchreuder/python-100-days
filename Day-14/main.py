from game_data import data
from art import logo, vs
from random import choice
import os

FIRST_OPTION = choice(data)
SECOND_OPTION = choice(data)
SCORE = 0


def play_game():
    global SCORE, FIRST_OPTION, SECOND_OPTION
    print(f"Compare A: {FIRST_OPTION['name']}, a {FIRST_OPTION['description']}, from {FIRST_OPTION['country']}.")
    print(vs)
    print(f"Against B: {SECOND_OPTION['name']}, a {SECOND_OPTION['description']}, from {SECOND_OPTION['country']}.")

    user_decision = input("Who has more followers? Type 'A' or 'B': ")

    os.system("clear")

    if user_decision == "A":
        if FIRST_OPTION["follower_count"] > SECOND_OPTION["follower_count"]:
            display_result(True)
            print("THIS MESSAGE")
            SECOND_OPTION = choice(data)
            return True
        elif FIRST_OPTION["follower_count"] < SECOND_OPTION["follower_count"]:
            display_result(False)
            print("False THIS MESSAGE")
            return False
        else:
            print(f"Tie current SCORE : {SCORE}")
            SECOND_OPTION = choice(data)
            print("Tie THIS MESSAGE")
            return True
    elif user_decision == "B":
        if FIRST_OPTION["follower_count"] < SECOND_OPTION["follower_count"]:
            display_result(True)
            FIRST_OPTION = SECOND_OPTION
            SECOND_OPTION = choice(data)
            return True
        elif FIRST_OPTION["follower_count"] > SECOND_OPTION["follower_count"]:
            display_result(False)
            return False
        else:
            print(f"Tie current SCORE : {SCORE}")
            SECOND_OPTION = choice(data)
            return True


def display_result(result):
    global SCORE
    if result:
        SCORE += 1
        print(f"You're right! Current SCORE: {SCORE}")
    else:
        print(f"Incorrect! Final SCORE: {SCORE}")


while True:
    print(logo)
    valid = play_game()
    if not valid:
        break
