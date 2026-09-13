import pygame


def checkSpot(player_data, mouse_pos):
    if player_data[mouse_pos[1] // 200][mouse_pos[0] // 200] == 1 or player_data[mouse_pos[1] // 200][mouse_pos[0] // 200] == 2:
        return True

def setSpot(player_data, mouse_pos, x):
    player_data[mouse_pos[1] // 200][mouse_pos[0] // 200] = x

def checkWin(player_data, x):
    win_detected = False

    # Check each horizontal row for win
    for i in range(3):
        for j in range(3):
            if player_data[i][j] != x:
                break
            elif j == 2:
                win_detected = True
                return win_detected

    for i in range(3):
        for j in range(3):
            if player_data[j][i] != x:
                break
            elif j == 2:
                win_detected = True
                return win_detected

    for i in range(3):
        if player_data[i][i] != x:
            break
        elif i == 2:
            win_detected = True
            return win_detected

    j = 0
    for i in range(2, -1, -1):
        if player_data[i][j] != x:
            break
        elif i == 0:
            win_detected = True
            return win_detected
        j += 1

    return win_detected