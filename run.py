import random
import string
from wordlist import words


def start_game():
    """
    This functions shows the instructions and
    starts the game when the user press enter.
    """
    print('==================================================================')
    print('"                         Welcome to HANGMAN                     "')
    print('"                                                                "')
    print('"  1.To the save the man from hanging you have to guess the word "')
    print('"  2.The word will be covered by hyphen "-"                      "')
    print('"  3.You have 7 tries to save the man from hanging               "')
    print('"  4.Press "Enter" after typing your guess                       "')
    print('"  5.You will not loose tries if you repeat your guess           "')
    print('"                                                                "')
    print('==================================================================')
    while input('Press "Enter" to start game\n') == "":
        play_game()


def get_valid_word(words_data):
    """
    Get random word from list of words in wordlist.py
    and will skip word if it has space or hyphen in it
    """
    word = random.choice(words_data)
    while '-' in word or ' ' in word:
        word = random.choice(words_data)
    return word.upper()


def play_again(data):
    """
    When the user has won or lost the game
    this function lets them choose if they want to play again.
    """
    if data == 0 or data is True:
        if input('Play again? (Y/N) \n').upper() == 'Y':
            play_game()


def play_game():
    """
    The actual game function
    The hangman game
    The user has 7 tries to guess what word is covered behing hyphens.
    Gets random word from get_valid_word() and uses it as the word that has
    to be guessed by the user.
    It collects all letters and words the user has guessed, and if the user
    guess the word or letter twice they get to try again.
    The function converts the game word and user input to uppercase letters.
    """
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()
    guessed_words = set()
    lives = 7
    all_word_letters = False

    while len(word_letters) > 0 and lives > 0:
        sketch(lives)
        print('You have used theese letters: ', ' '.join(guessed_letters))
        print(word)
        print(f'You have {lives}lives left')

        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_input = input('Guess the full word or with one letter:\n').upper()
        print(user_input)
        if len(user_input) == 1:
            if user_input in alphabet - guessed_letters:
                guessed_letters.add(user_input)
                if user_input in word_letters:
                    word_letters.remove(user_input)
                    print('The letter is in the word')
                else:
                    lives -= 1
                    guessed_letters.add(user_input)
                    print('The letter is not in the word')
            elif user_input in guessed_letters:
                print('You have already guessed this letter')
            else:
                print("Invalid characters, try again!")
        elif len(user_input) == len(word):
            if user_input in guessed_words:
                print('You have already guessed that word, try again!')
            elif user_input != word:
                print(f'{user_input} is incorrect')
                lives -= 1
                guessed_words.add(user_input)
            else:
                word_letters.clear()
                all_word_letters = True
                print('Correct answer')
    if all_word_letters:
        print('win')
        play_again(all_word_letters)
    else:
        print('loose')
        print(sketch(0))
        play_again(lives)


def sketch(lives):
    """
    This functions shows the hangman be created step by step
    depending on how many lives the user has
    """
    if lives == 0:
        print('\n                   Better luck next time                    ')
        print('==============================================================')
        print('"                                                            "')
        print('"                          ________                          "')
        print('"                          |      |                          "')
        print('"                          o      |                          "')
        print('"                         /|\     |                          "')
        print('"                         / \     |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('==============================================================')

    elif lives == 1:
        print('\n                        You have 1 lives                  \n')
        print('==============================================================')
        print('"                                                            "')
        print('"                          ________                          "')
        print('"                          |      |                          "')
        print('"                          o      |                          "')
        print('"                         /|\     |                          "')
        print('"                         /       |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('==============================================================')
    elif lives == 2:
        print('\n                        You have 2 lives                  \n')
        print('==============================================================')
        print('"                                                            "')
        print('"                          ________                          "')
        print('"                          |      |                          "')
        print('"                          o      |                          "')
        print('"                         /|\     |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('==============================================================')
    elif lives == 3:
        print('\n                        You have 3 lives                  \n')
        print('==============================================================')
        print('"                                                            "')
        print('"                          ________                          "')
        print('"                          |      |                          "')
        print('"                          o      |                          "')
        print('"                         /|      |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('==============================================================')
    elif lives == 4:
        print('\n                        You have 4 lives                  \n')
        print('==============================================================')
        print('"                                                            "')
        print('"                          ________                          "')
        print('"                          |      |                          "')
        print('"                          o      |                          "')
        print('"                         /       |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('==============================================================')
    elif lives == 5:
        print('\n                        You have 5 lives                  \n')
        print('==============================================================')
        print('"                                                            "')
        print('"                          ________                          "')
        print('"                          |      |                          "')
        print('"                          o      |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('==============================================================')
    elif lives == 6:
        print('\n                        You have 6 lives                  \n')
        print('==============================================================')
        print('"                                                            "')
        print('"                          ________                          "')
        print('"                          |      |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('==============================================================')
    elif lives == 7:
        print('\n                        You have 7 lives                  \n')
        print('==============================================================')
        print('"                                                            "')
        print('"                          ________                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('"                                 |                          "')
        print('==============================================================')


def main():
    """
    This functions starts the game
    """
    start_game()


main()
