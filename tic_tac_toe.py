import random

X = "X"
O = "O"
EMPTY = " "
COUNT = 9
COMBINATIONS_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )

def create_board(): #creates initial board
    board = []
    for i in range(9):
        board.append(EMPTY)
    return board

def write_board(board): #writes the board in convenient way
    print('\n')
    print(board[0],'|', board[1], '|', board[2])
    print('-'*10)
    print(board[3],'|', board[4], '|', board[5])
    print('-'*10)
    print(board[6],'|', board[7], '|', board[8])

def hum_comp():
    answer=input('Do you want to start the game? (y/n): ')
    if answer.lower() == 'y':
        human = X
        comp = O
    else:
        human = O
        comp = X
    return (human, comp)

def possible_moves(board): #Creates a list of possible moves"
    moves = []
    for index,cell in enumerate(board):
        if cell == EMPTY:
            moves.append(index)
    return moves

def human_step(board): #process the human step
    moves=possible_moves(board)
    step = int(input('Choose the empty cell [0-8]: '))
    while step not in moves:
        step = int(input('This cell is not empty, choose another one: '))
    return step

def winner(board): # who is the winner?
    for i in COMBINATIONS_WIN:
        if board[i[0]] == board[i[1]] == board[i[2]] != EMPTY:
            winner = board[i[0]]
            return winner
    if EMPTY not in board:
        d = 'Draw'
        return d

def computer_step(board, computer, human): #process computer step
    board = board[:]
    print("Computer's step: ")
    for s in possible_moves(board):
        board[s] = computer
        if winner(board) == computer:
            print(s)
            return s
        board[s] = EMPTY
    for s in possible_moves(board):
        board[s] = human
        if winner(board) == human:
            print(s)
            return s
        board[s] = EMPTY
    step = random.choice(possible_moves (board))
    print(step)
    return step
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

def main():
    print("""To perform step it is necessary to insert the number according \n
    to the following table:

    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    """)
    human , computer = hum_comp()
    turn = X
    board = create_board()
    write_board(board)
    while not winner(board):
        if turn == human:
            step = human_step(board)
            board[step] = human
        else:
            step = computer_step(board, computer, human)
            board[step] = computer
        write_board(board)
        turn = next_turn(turn)
        theWinner = winner(board)
    if theWinner == computer:
        print("Computer won")
    elif theWinner == "Draw":
        print("Draw")
    else:
        print("You won")


if __name__ == '__main__':
    main()
