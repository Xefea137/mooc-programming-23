# Write your solution here
def who_won(game_board: list):
    player_1 = 0
    player_2 = 0
    for row in game_board:
        for value in row:
            if value == 1:
                player_1 += 1
            elif value == 2:
                player_2 += 1
    if player_1 > player_2:
        return 1
    elif player_2 > player_1:
        return 2
    else:
        return 0

if __name__ == "__main__":
    print(who_won([[1, 2, 2, 2], [0, 0, 0, 1], [0, 0, 2, 1]]))