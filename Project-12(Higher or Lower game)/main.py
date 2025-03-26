from game_data import data
import random
from art import logo,vs


def game():
    value1 = generate()
    value2 = generate()
    current_score = 0
    show(value1,value2)
    while True:
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        #result(option, value1, value2)
        if choice == compare(value1,value2):
            current_score += 1
            value3 = generate()
            value1 = value2
            value2 = value3
            print("\n"*15)
            print(f"You're right, your current score is: {current_score}")
            show(value1,value2)


        else:
            print(logo)
            print(f"Sorry! that's wrong, your final score is: {current_score}")
            break


def generate():
    v = random.choice(data)
    return v


def show(val1,val2):
    print(logo)
    print(f"Compare A: {val1['name']}, a {val1["description"]}, from {val1["country"]}")
    print(vs)
    print(f"Against B: {val2['name']}, a {val2["description"]}, from {val2["country"]}")


def compare(val1,val2):
    if val1['follower_count'] > val2['follower_count']:
        return "A"
    else:
        return "B"


game()
