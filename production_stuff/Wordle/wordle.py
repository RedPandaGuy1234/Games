import warnings
warnings.filterwarnings('ignore', message='urllib3 v2 only supports OpenSSL')
import requests
import sys
import random
import urllib3
urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)

txt_url = "https://raw.githubusercontent.com/RedPandaGuy1234/Games/refs/heads/main/production_stuff/Wordle/Valid_Words.txt"
response = requests.get(txt_url)

if response.status_code == 200:
    Valid_Words = response.text.splitlines()
else:
    Valid_Words = []
    print("This code has failed because the list for valid words did not show up. Please alert RedPandaGuy1234 of this. Thank you!")
    sys.exit(1)

txt_url = "https://raw.githubusercontent.com/RedPandaGuy1234/Games/refs/heads/main/production_stuff/Wordle/Word_Bank.txt"
response = requests.get(txt_url)

if response.status_code == 200:
    Word_bank = response.text.splitlines()
else:
    Word_bank = []
    print("This code has failed because the list for the word bank did not show up. Please alert RedPandaGuy1234 of this. Thank you!")
    sys.exit(1)

Word = Word_bank[random.randint(1, 2314)]
Guess = "This is a filler!"
guesses = 0
is_guess_incorrect = True

def guess_word(guesses):
    guesses = guesses + 1
    guessed_word = input("Hello! Please enter your word, and use all lowercase.")
    if guessed_word not in Valid_Words:
        print("Sorry, but either you used an uppercase character, it is not in the Valid word bank (this is a limited word bank, and does not have every single five letter work in the world), you typed a space anywhere, it is not five letters, or this is not a word. Please try again.")
        guess_word(guesses)
    else:
        print("Ok!")
        char_word_list = set(guessed_word)
        return char_word_list, guesses

def check_word(guesses, Guess):
    
    while is_guess_incorrect:
        Guess, guesses = guess_word(guesses)

