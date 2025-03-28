import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {rows.letter: rows.code for index,rows in data.iterrows()}
print(phonetic_dict)

while True:
    is_true = 0
    user_input = input("enter a word: ").upper()
    try:
        new_list = [phonetic_dict[char] for char in user_input if char != " "]
    except :
        print("Sorry, only letters in the alphabet please.")
        is_true = 1

    if is_true == 0:
        print(new_list)
        break
