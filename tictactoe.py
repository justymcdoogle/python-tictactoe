import os

# print the board
def print_board(board):
    print( 
    board[0] + '|' + board[1] + '|' + board[2] + '\n' +
    board[3] + '|' + board[4] + '|' + board[5] + '\n' +
    board[6] + '|' + board[7] + '|' + board[8]
    )


# handle a turn
def one_turn():
    while True:
        try:
            player_turn = int(input("Please enter a number between 1 and 9: "))
            if 1 <= player_turn <= 9:
                return player_turn
        except ValueError:
            continue

# mark a spot
def mark_spot(board, turn, symbol):
    if board[turn - 1] != '-':
        return False
    else:
        board[turn - 1] = symbol
        return True


def game_loop(board):
    
    SYMBOL_1 = 'x'
    SYMBOL_2 = 'o'

    turn_counter = 0
    is_winner = False

    while not is_winner:

        if turn_counter % 2 == 0:
            symbol = SYMBOL_1
        else:
            symbol = SYMBOL_2

        print(f"{symbol}'s turn")

        # get spot number from input
        turn = one_turn()

        # update board list
        result = mark_spot(board, turn, symbol)

        # only increment if valid move
        if result:
            turn_counter += 1

        # clear the screen
        os.system('clear')

        # win handler
        is_winner = check_winner(board, symbol)

        # print (potentially) updated board
        print_board(board)
        if is_winner:
            break

        # invalid move handler
        if not result:
            print("Spot already taken")


        # tie handler
        if '-' not in board:
            os.system('clear')
            print_board(board)
            print("Tie!")
            exit()

    print(f'{symbol} wins!')


# check winner
def check_winner(board, symbol):

    if (
    # horizonals for x
        (board[0] == symbol and board[1] == symbol and board[2] == symbol) or 
        (board[3] == symbol and board[4] == symbol and board[5] == symbol) or 
        (board[6] == symbol and board[7] == symbol and board[8] == symbol) or 
    # verticals for x
        (board[0] == symbol and board[3] == symbol and board[6] == symbol) or 
        (board[1] == symbol and board[4] == symbol and board[7] == symbol) or 
        (board[2] == symbol and board[5] == symbol and board[8] == symbol) or 
    # diagonals for x
        (board[0] == symbol and board[4] == symbol and board[8] == symbol) or 
        (board[2] == symbol and board[4] == symbol and board[6] == symbol)):
        return True
    
    else:
        return False


def main():

    board = [
        "-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"
    ]
    
    # show inital board before game starts
    os.system('clear')
    print_board(board)
    ## print("X's turn.")
    # actual game loop
    game_loop(board)



if __name__ == "__main__":
    main()
