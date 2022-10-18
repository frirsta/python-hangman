# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import string
import gspread
from wordlist import words
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("python_hangman")

high_scores = SHEET.worksheet('high_scores')


def get_valid_word(words_data):
    word = random.choice(words_data)
    while '-' in word or ' ' in word:
        word = random.choice(words_data)
    return word.upper()


def play_game():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()
    guessed_words = set()
    lives = 10

    while len(word_letters) > 0 and lives > 0:
        print('You have used theese letters: ', ' '.join(guessed_letters))

        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_input = input('Guess the full word or with one letter:  \n').upper()
        print(user_input)
        if len(user_input) == 1:
            if user_input in alphabet - guessed_letters:
                guessed_letters.add(user_input)
                if user_input in word_letters:
                    word_letters.remove(user_input)
                    print('Correct letter')
            elif user_input in guessed_letters:
                print('You have already guessed this letter')
            else:
                print("Invalid characters, try again!")



play_game()
# elif len(user_input) == len(full_word) and user_input is alpha():
#         if user_input in guessed_words:
#             print('You have already guessed this word!')
#             else:
#                 lives = - 1
#                 print(f'The letter is not in the word. You have {lives}lives left!')