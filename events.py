import pygame

def checkSpot(player_data, mouse_pos):
    if player_data[mouse_pos[1] // 200][mouse_pos[0] // 200] == 1 or player_data[mouse_pos[1] // 200][mouse_pos[0] // 200] == 2:
        return True

def setSpot(player_data, mouse_pos, x):
    player_data[mouse_pos[1] // 200][mouse_pos[0] // 200] = x