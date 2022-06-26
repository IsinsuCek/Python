from itertools import cycle
game_board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
def diagonal_win(game_board):
    size = len(game_board)
    if game_board[0][0] != 0 and all(game_board[x][x] == game_board[0][0] for x in range(size)):
       return True

def second_diagonal_win(game_board):
    max_index = len(game_board)
    if game_board[max_index][0] != 0:
        if all(game_board[i][j] == game_board[max_index][0] for i, j , in zip(range(max_index), range(max_index, 0, -1))):
            return True




def vertical_win(game_board):
    size = len(game_board)
    for vertical in range(size):
        if game_board[vertical][0] != 0:
            if all(game_board[0][vertical] == game_board[i][vertical] for i in range(size)):
                return True
print(vertical_win(game_board))



def horizontal_win(game_board):
    size = len(game_board)
    for horizon in range(size):
        #horizon[0] == horizon[1] and horizon[0] == horizon[2]
        if all(x == horizon[0] for x in horizon):
            return True

def is_win(game_board):
    win_con = [horizontal_win(game_board), vertical_win(game_board), diagonal_win(game_board), second_diagonal_win(game_board)]
    if any(win_con):
        return True


IS_WIN = False
player_list = cycle([1,2])

while not IS_WIN:
  
    current_player = next(player_list)
    for i in game_board:
        print(i)
    current_place  = input("{} player".format(current_player))
    row, col = list(map(int, current_place.split(',')))

    inpt_try = game_board[row][col]
    if inpt_try == 0:
        game_board[row][col] = current_player
    else:
        print('not valid')
        current_place  = next(player_list)
    if is_win(game_board):
        print('winner {}'.format(current_player))
        break
    print(game_board)