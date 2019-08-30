import random

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves in a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field(): #is used to create a random field in the beginning of the game
    field=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,EMPTY_MARK]
    random.shuffle(field)
    return field

def print_field(field): #This method prints field to user
    for i in range(0, 16, 4):
        print(field[i:i + 4])
    print('\n')


def is_game_finished(field): #checking if the game is finished
    if field == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,EMPTY_MARK]:
        return True
    else:
        return False

def perform_move(field, key): #performs moves
    i = field.index(EMPTY_MARK)
    if i in range(0,4) and key == 'w':
        raise IndexError('The move cannot be done')
    elif i in range(12,16) and key == 's':
        raise IndexError('The move cannot be done')
    elif i in (0,4,8,12) and key == 'a':
        raise IndexError('The move cannot be done')
    elif i in (3,7,11,15) and key == 'd':
        raise IndexError('The move cannot be done')
    a = field[i]
    b = field[i + MOVES[key]]
    field[i] = b
    field[i + MOVES[key]] = a
    return field

def handle_user_input():
    key = input('Use the commands WSAD to move the empty tile on the field: ')
    return key

def main():
    try:
        c=0 #counter : indicates number of steps user performes
        current_field = shuffle_field()
        print_field(current_field)
        while is_game_finished(current_field) == False:
            try:
                step = handle_user_input()
                current_field = perform_move(current_field,step)
                c+=1
                print_field(current_field)
            except IndexError as i:
                print('Ooops..', i)
        print('Bravo! Game is over! You did it in {} steps! '.format(c))
    except KeyboardInterrupt :
        print('\n')
        print('shutting down')

if __name__ == '__main__':

    main()
