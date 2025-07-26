#Project Given by Ayaan

import random
import requests
import string

score = 0
total_score = 0

def generate_letters():
    global used_words
    global letters
    used_words = []
    letters = []
    letters = random.sample(string.ascii_uppercase, 7)
    print("Here is your list")
    print(letters)

def word_valid2(word):
    global letters
    upper_word = word.upper()
    if len(upper_word) > 7:
        return False
    if len(word) != len(set(upper_word)):
        return False
    for letter in upper_word:
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
    global score
    global total_score
    score = len(word) * 10
    total_score = total_score + score
    

print("Welcome to your Word Quiz game." + "\n")
print("The rules are, you must use the letters shown on screen to you")
print("The word must be an actual word and you are not allowed to use the same letter twice." + "\n")
print("The word length will be multiplied by by 10 and thats the amount of points you get for each word.")
print("Type _end_ whenever you want to quit")
print("lets start")

generate_letters()

shit = True
while shit == True:
    user_word = str(input("Enter your word: "))
    if user_word == "_end_":
        shit = False
    if (is_valid_word(user_word) == True) and (word_valid2(user_word) == True) and (user_word not in used_words):
        calculate_score(user_word)
        print("That is a correct word.")
        print(f"Your current score is {total_score}")
        used_words.append(user_word)
    else:
        print("Invalid word. Try again")
    while True:
        try:
            print("Type continue if you have more words or type next for a" + "\n " +"new set of letters.")
            user_choice = input("Your choice: ")
            if user_choice.lower() == "next":
                generate_letters()
                break
            elif user_choice == "_end_":
                shit = False
                break
            elif user_choice == "continue":
                shit = True
                break
            else:
                print("Invalid choice, Try again")
        except ValueError:
            print("Enter either continue, next or _end_")

print(f"This is your final score {total_score}")
print("Thanks for playing, see you next time.")