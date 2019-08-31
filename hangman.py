import random

WORDS = ['hangman','table','satisfaction','pleasure','python','apple','water']

MAX_ERRORS = 8

def gen_word(): #choose randomly the word
    return random.choice(WORDS)


def guess_letter(): #handle user's input
    user_input = input('Try to guess the letter: ')
    return user_input

def initial_stat(word): #initial status of every letter in the word
    statuses = []
    for letter in word:
        statuses.append(False)
    return statuses

def game_over(statuses,current_errors): #checking if the game is over
    if current_errors >= MAX_ERRORS:
        return True
    for status in statuses:
        if not status:
            return False
    return True


def perform_action(word, statuses, letter):
    if letter not in word:
        return False
    for index,l in enumerate(word):
        if letter ==l:
            statuses[index] = True
    return True

def print_word(word, statuses):
    for index, letter in enumerate(word):
        if statuses[index]:
            print(letter, end=' ')
        else:
            print('_', end=' ')


def main():
    word = gen_word()
    statuses = initial_stat(word)
    errors = 0

    while not game_over(statuses,errors):
        print_word(word,statuses)
        print('Errors left: ', MAX_ERRORS - errors)
        letter = guess_letter()
        result = perform_action(word,statuses,letter)
        if not result:
            errors+=1
    if errors >= MAX_ERRORS:
        print('You lose!')
    else:
        print('You win! ')


if __name__ == '__main__':
    main()
