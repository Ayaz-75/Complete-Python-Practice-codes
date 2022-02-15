import random

HARD_LEVEL = 5
EASY_LEVEL = 10


def check_numbers(user_guess, random_number, turns):
    if user_guess > random_number:
        print("Too High")
        return turns - 1
    elif user_guess < random_number:
        print("Too Low")
        return turns - 1
    else:
        print(f"perfect ! you got it answer was {random_number}")


def set_level():
    level = input("Choose Difficulty: ")
    if level == "hard":
        return HARD_LEVEL
    else:
        return EASY_LEVEL


def game():
    print("----- Welcome to the Guessing Number Game ------")
    print("i am thinking a number between 1 and 100")
    random_number = random.randint(1, 100)
    print(random_number)

    user_guess = 0

    turns = set_level()
    while user_guess != random_number:
        print(f"you have {turns}, attempts remaining")
        user_guess = int(input("Make a Guess: "))
        turns = check_numbers(user_guess, random_number, turns)
        if turns == 0:
            print("You ran out of moves you loose")
            return


game()
