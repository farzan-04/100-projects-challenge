import random
import art

def check_guessing(guess_number,correct_number):
    if guess_number > correct_number:
        print("Too High.")
        return 0
    elif guess_number < correct_number:
        print("Too Low.")
        return 0
    else:
        print(f"YOU WON!, you guessed the correct number {correct_number}")
        return 1


def game(difficulty, correct_number):
    if difficulty == "easy":
        attempts = 10
        while attempts >= 1:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess_number = int(input("Make a guess: "))
            if check_guessing(guess_number, correct_number):
                return
            else:
                print("Guess again.")
                attempts -= 1
        print("YOU LOST!, You've run out of guesses. Refresh the page to run again. ")

    else:
        attempts = 5
        while attempts >= 1:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess_number = int(input("Make a guess: "))
            if check_guessing(guess_number, correct_number):
                return
            else:
                attempts -= 1
                if attempts != 0:
                    print("Guess again.")
        print("YOU LOST!, You've run out of guesses. Refresh the page to run again. ")




actual_number = random.randint(1, 100)
print(art.logo)
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()

game(level, actual_number)

