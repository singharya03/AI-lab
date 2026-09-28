

board = [' '] * 9

combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    for combination in combinations:
        if (board[combination[0]] == player and
            board[combination[1]] == player and
            board[combination[2]] == player):
            return True
    return False

def check_draw():
    return ' ' not in board

player = 'X'

while True:
    print_board()

    position = int(input("Enter position (1-9): "))
    
    if position < 1 or position > 9:
        print("Enter a number between 1 and 9.")
        continue

    if board[position - 1] != ' ':
        print("Position already taken.")
        continue

    board[position - 1] = player

    if check_winner(player):
        print_board()
        print(player, "wins!")
        break

    if check_draw():
        print_board()
        print("It's a draw!")
        break

    if player == 'X':
        player = 'O'
    else:
        player = 'X'