import random
import string
from wordlist import words


def start_game():
    """
    This functions shows the instructions and
    starts the game when the user press enter.
    """
    print('                                                                  ')
    print('                                                                  ')
    print('                                                                  ')
    print('                                                                  ')
    print('                                                                  ')
    print('==================================================================')
    print('"                         Welcome to HANGMAN                     "')
    print('"                                                                "')
    print('"  1.To the save the man from hanging you have to guess the word "')
    print('"  2.The word will be covered by hyphens "-"                     "')
    print('"  3.You have 7 tries to save the man from hanging               "')
    print('"  4.Press "Enter" after typing your guess                       "')
    print('"  5.You will not loose tries if you repeat your guess           "')
    print('"                                                                "')
    print('==================================================================')
    print('                                                                  ')
    print('                                                                  ')
    print('                                                                  ')
    print('                                                                  ')
    if input('Press "Enter" to start game\n\n\n') == "":
        play_game()
    else:
        play_game()


def get_valid_word(words_data):
    """
    Get a random word from the list of words in wordlist.py
    and will skip word if it has a space or hyphen in it
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
        if input('\n========================================\n"                                      "\n" Enter "Y" to play again              "\n"                                      "\n"                                      "\n" Press "Enter" to return to Home page "\n"                                      "\n"                                      "\n========================================\n\n\n\n\n\n').upper() == 'Y':
            play_game()
        else:
            return start_game()


def play_game():
    """
    The actual game function
    The hangman game
    The user has 7 tries to guess what word is covered behind hyphens.
    Gets random word from get_valid_word() and uses it as the word that has
    to be guessed by the user.
    It collects all letters and words the user has guessed, and if the user
    guesses the word or letter twice they get to try again.
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
        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        print('\nYou have used theese letters: ', ' '.join(guessed_letters))

        user_input = input('\nGuess the full word or with one letter:\n').upper()
        if len(user_input) == 1:
            if user_input in alphabet - guessed_letters:
                guessed_letters.add(user_input)
                if user_input in word_letters:
                    word_letters.remove(user_input)
                    print('\n\nThe letter is in the word!')
                    if len(word_letters) == 0:
                        all_word_letters = True
                else:
                    lives -= 1
                    guessed_letters.add(user_input)
                    print('\nThe letter is not in the word')
            elif user_input in guessed_letters:
                print('\nYou have already guessed this letter')
            else:
                print('\nInvalid characters, try again!')
        elif len(user_input) == len(word) and user_input.isalpha():
            if user_input in guessed_words:
                print('\nYou have already guessed that word, try again!')
            elif user_input != word:
                print(f'\n{user_input} is incorrect')
                lives -= 1
                guessed_words.add(user_input)
            else:
                word_letters.clear()
                all_word_letters = True
        else:
            print('\nInvalid characters, try again!')
    if all_word_letters:
        print(f'\n\n\n\n\nCongratulations, you guessed the correct word!\n{word}\n')
        play_again(all_word_letters)
    else:
        print(sketch(0))
        print(f'\n\n\n\n\nYou lose better luck next time!\nThe word was {word}\n')
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
        print('                                                              ')
        print('                                                              ')
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
        print('                                                              ')
        print('                                                              ')
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
        print('                                                              ')
        print('                                                              ')
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
        print('                                                              ')
        print('                                                              ')
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
        print('                                                              ')
        print('                                                              ')
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
        print('                                                              ')
        print('                                                              ')
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
        print('                                                              ')
        print('                                                              ')
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
        print('                                                              ')
        print('                                                              ')


def main():
    """
    This functions starts the game
    """
    start_game()


main()
