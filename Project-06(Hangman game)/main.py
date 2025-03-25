import random
from hangman_words import *

lives = 6

from hangman_art import *
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"{lives}/6 LIVES LEFT")
    guess = input("Guess a letter: ").lower()

    display = []

    for letter in chosen_word:
        if letter == guess:
            display.append(letter)
            correct_letters.append(letter)
        elif letter in correct_letters:
            display.append(letter)
        else:
            display.append("_")
    display = ''.join(display)
    if guess in correct_letters:
        print("You have already guessed", guess)
    print("Word to guess: ", display)


    if guess not in chosen_word:
        lives -= 1
        print("you guessed ",guess, ", thats not in the word. you lose a life")

        if lives == 0:
            game_over = True

          
            print("It was", chosen_word,"! YOU LOSE")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

  
    print(stages[lives])
