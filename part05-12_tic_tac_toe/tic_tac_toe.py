# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if y < 0 or y >= len(game_board) or x < 0 or x >= len(game_board[0]) or game_board[y][x] != "":
        return False
    game_board[y][x] = piece
    return True

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)
    game_board = [['X', '', ''], ['O', 'O', 'O'], ['', 'O', '']]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)