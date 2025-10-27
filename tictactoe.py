# print the board

def print_board(board):
    print( 
    board[0] + '|' + board[1] + '|' + board[2] + '\n' +
    board[3] + '|' + board[4] + '|' + board[5] + '\n' +
    board[6] + '|' + board[7] + '|' + board[8]
    )

# create a board
board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]


print_board(board)


# handle a turn
while True:
    try:
        player_turn = int(input("Please enter a number between 1 and 9: "))
        if 1 <= player_turn <= 9:
            break
    except:
        continue

# keep asking for turns and switch x and o
# verify winner
    # 3 in a row horizontally
    # 3 in a row vertically
    # 3 in a row diagonally
# if no winner, tie

