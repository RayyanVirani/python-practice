#Project Given by Ayaan

import random
import requests

Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letters = []

def generate_letters():
    while len(letters) != 7:
        random_letter = random.choice(Alphabet)
        if random_letter != letters:
            letters.append(random_letter)
    print(letters)

def is_valid_word(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

generate_letters()
user_word = input()
print(is_valid_word(user_word))