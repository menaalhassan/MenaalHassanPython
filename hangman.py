print(" ------------------------------------------------") 
print("|                                                |")
print("|                                                |")
print("|    Welcome to a game of Hangman!!!             |")
print("|                                                |")
print("|                                                |")
print(" ------------------------------------------------")

from random import choice

words = ["hello", "there", "school", "food", "ist", "IST", "clothes", "eid", ""]

chosen_word = choice(words)

#underscore is length of the chosen word
displayed_word = '_' * len(chosen_word)

print(displayed_word)

TOTAL_ALLOWED_GUESS = 18

for x in range(TOTAL_ALLOWED_GUESS):
    guess_letter = input("Guess a letter: ")

    if guess_letter in chosen_word:
        offset = 0
        while offset < len(chosen_word):
            try:
                i = chosen_word.index(guess_letter, offset)
                offset = i + 1
                displayed_word = displayed_word[:i] + guess_letter + displayed_word[i+1:]
            except ValueError as e:
                break    

    print(displayed_word)

    if '_' not in displayed_word:
        print("Congratulations! YOU WON!")
        break