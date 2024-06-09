import random
from art import logo
print(logo)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess,number, turns):
    """checks answer against guess and returns the number of turns remaining"""
    if guess > number:
        print ("Too high!")
        return turns - 1
    elif guess < number:
        print("Too low!")
        return turns - 1
    else:
        print(f"you got it! The answer was {number}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy" :
        global turn
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
def game():
    print("Welcome to the number Guess Game!")
    print("I'm thinking the number between 1 and 100")

    answer = random.randint(1, 100)
   # print(f"the corrrect answer is {answer}")


    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess :"))
        turns = check_answer(guess,answer, turns)
        if turns == 0 :
           print("You've run out of guesses, you lose.")
           return
        elif guess != answer:
            print("Guess again")
game()
