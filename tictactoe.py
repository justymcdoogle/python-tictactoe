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
        except:
            continue

# mark a spot
def mark_spot(board, turn, turn_counter):
    if board[turn - 1] != '-':
        return False
    if turn_counter % 2 == 0:
        board[turn - 1] = 'x'
        return True
    else:
        board[turn - 1] = 'o'
        return True


def game_loop(board):
    
    turn_counter = 0
    is_winner = False

    while not is_winner:
        # get spot number from input
        turn = one_turn()
        # update board
        result = mark_spot(board, turn, turn_counter)
        # only increment if valid move
        if result:
            turn_counter += 1

        os.system('clear')
        is_winner = check_winner(board)
        print_board(board)

        if not result:
            print("Spot already taken")

        if '-' not in board:
            print("Tie!")
            exit()


# check winner
def check_winner(board):

    # horizonals
    if (board[0] == 'x' and board[1] == 'x' and board[2] == 'x') or (board[0] == 'o' and board[1] == 'o' and board[2] == 'o'):
        return True
    if (board[3] == 'x' and board[4] == 'x' and board[5] == 'x') or (board[3] == 'o' and board[4] == 'o' and board[5] == 'o'):
        return True
    if (board[6] == 'x' and board[7] == 'x' and board[8] == 'x') or (board[6] == 'o' and board[7] == 'o' and board[8] == 'o'):
        return True

    # diagonals
    if (board[0] == 'x' and board[4] == 'x' and board[8] == 'x') or (board[0] == 'o' and board[4] == 'o' and board[8] == 'o'):
        return True
    if (board[2] == 'x' and board[4] == 'x' and board[6] == 'x') or (board[2] == 'o' and board[4] == 'o' and board[6] == 'o'):
        return True

    # verticals
    if (board[0] == 'x' and board[3] == 'x' and board[6] == 'x') or (board[0] == 'o' and board[3] == 'o' and board[6] == 'o'):
        return True
    if (board[1] == 'x' and board[4] == 'x' and board[7] == 'x') or (board[1] == 'o' and board[4] == 'o' and board[7] == 'o'):
        return True
    if (board[2] == 'x' and board[5] == 'x' and board[8] == 'x') or (board[2] == 'o' and board[5] == 'o' and board[8] == 'o'):
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
    print_board(board)
    # actual game loop
    game_loop(board)



if __name__ == "__main__":
    main()
