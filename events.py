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


def startScreen(screen):

    # Load fonts
    font1 = pygame.font.Font('freesansbold.ttf', 32)
    font2 = pygame.font.Font('freesansbold.ttf', 56)

    # Create text objects
    startGameText = font1.render('Start game?', True, "black", None)
    gameTitleText = font2.render('Tic Tac Toe!', True, "blue", None)
    yesText = font1.render('Yes', True, "white", None)
    noText = font1.render('No', True, "white", None)

    screen.fill("white")
    screen.blit(gameTitleText, (141, 100))
    screen.blit(startGameText, (205, 200))
    pygame.draw.rect(screen, "green", (130, 250, 150,50))
    pygame.draw.rect(screen, "red", (320, 250, 150,50))
    screen.blit(yesText, (178, 259))
    screen.blit(noText, (373.5, 259))
    pygame.display.flip()


def gameEnd(screen):

    # Load fonts
    font1 = pygame.font.Font('freesansbold.ttf', 32)

    # Create text objects
    yesText = font1.render('Yes', True, "white", None)
    noText = font1.render('No', True, "white", None)

    playAgainText = font1.render('Play again?', True, "black", None)
    screen.fill("white")
    screen.blit(playAgainText, (208,150))
    pygame.draw.rect(screen, "green", (130, 250, 150,50))
    pygame.draw.rect(screen, "red", (320, 250, 150,50))
    screen.blit(yesText, (178, 259))
    screen.blit(noText, (373.5, 259))
    pygame.display.flip()