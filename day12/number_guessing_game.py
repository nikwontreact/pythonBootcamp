import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_answer,actual_answer,turns):
    """checks answer against guess. returns remaining no of turns"""
    if user_answer < actual_answer:
        print("Too low ") 
        return turns -1
    elif user_answer > actual_answer:
        print("Too high")
        return turns -1
    else:
        print(f"You got it. the answer was {actual_answer} ")

def set_level():
    """ set the difficulty level for game"""
    level=  input("choose the difficulty level type 'easy' or 'hard' ").lower()
    if level == "easy":
       return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Invalid input. Easy level set by default. ")
        return EASY_LEVEL_TURNS
    
# starting game 
def game():
    print('Welcome to the number guessing game !!! ')
    print("I'm thinking of a number from 1 to 100 ")

    answer = random.randint(1,100)
    turns = set_level()

    # Let user guess 
    guess = 0
    while guess != answer:
        print(f"You have {turns} remaining to guess the number.")
        guess = int(input("Make a guess "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You lost. you ran outta guesses")
            return print(f"Answer was {answer}")
        elif guess != answer:
            print(f"Wrong guess. you have {turns} remaining")
game()

