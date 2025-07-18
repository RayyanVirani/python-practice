#Project Given by Ayaan

import random
import requests

Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letters = []
score = 0

def generate_letters():
    while len(letters) != 7:
        random_letter = random.choice(Alphabet)
        if random_letter != letters:
            letters.append(random_letter.upper())
    print("Here is your list")
    print(letters)

def word_valid2(word):
    lower_word = word.lower()
    if len(lower_word) > 7:
        return False
    if len(word) != len(set(lower_word)):
        return False
    for letter in lower_word:
        if letter not in letters:
            return False
    return True

def is_valid_word(word):
    lower_word = word.lower()
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + lower_word
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False
    
def calculate_score(word):
    score = len(word) * 10
    

print("Welcome to your Word Quiz game." + "\n")
print("The rules are, you must use the letters shown on screen to you")
print("The word must be an actual word and you are not allowed to use the same letter twice." + "\n")
print("The word length will be multiplied by by 10 and thats the amount of points you get for each word.")
print("Type _end_ whenever you want to quit")
print("lets start")

generate_letters()

while True:
    user_word = str(input("Enter your word: "))
    if user_word == "_end_":
        break
    if (is_valid_word(user_word) == True) and (word_valid2(user_word) == True):
        calculate_score(user_word)
        print("That is a correct word.")
        print(f"Your correct score is {score}")
    else:
        print("Invalid word. Try again")
    print("Type continue if you have more words or type next for a new set of letters.")
    user_choice = input("Your choice:")
    if user_choice.lower() == "next":
        generate_letters()
    elif user_choice == "_end_":
        break

print(f"This is your final score {score}")
print("Thanks for playing, see you next time.")