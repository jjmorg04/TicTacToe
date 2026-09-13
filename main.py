# Tic Tac Toe Game
import pygame
from board import Board
from events import checkSpot, setSpot, checkWin

# Player data on game start -> all empty
player_data = [[0,0,0],[0,0,0],[0,0,0]]
test_data = [[1,0,0], [0,1,0], [0,0,1]]

# Set window name
pygame.display.set_caption("Tic Tac Toe!")

pygame.init() # Initialize pygame instance
pygame.font.init() # Initialize pygame font instance
screen = pygame.display.set_mode((600,600)) # Create screen w/ resolution
clock = pygame.time.Clock() # Create clock variable using pygame's built-in clock
running = True # Game state is set to running

p1_turn = True # Tic-tac-toe turn base starting w/ p1

x_img = pygame.image.load('X.png').convert() # load & convert X icon
o_img = pygame.image.load('O.png').convert() # load & convert O icon

# Initiate board object
board = Board()

# Create counter variable to later keep track of turn
ctr = 1

# Pygame may be running, but game logic isn't yet (wait for start screen)
game_start = False

# Pygame loop until game is ended
while running:


    font1 = pygame.font.Font('freesansbold.ttf', 32)
    font2 = pygame.font.Font('freesansbold.ttf', 56)
    startGameText = font1.render('Start game?', True, "black", None)
    gameTitleText = font2.render('Tic Tac Toe!', True, "blue", None)
    yesText = font1.render('Yes', True, "white", None)
    noText = font1.render('No', True, "white", None)

    yesRect = pygame.Rect(130,250,150,50)
    noRect = pygame.Rect(320,250,150,50)

    plyrStart = False
    while(not plyrStart):    
        screen.fill("white")
        screen.blit(gameTitleText, (141, 100))
        screen.blit(startGameText, (205, 200))
        pygame.draw.rect(screen, "green", (130, 250, 150,50))
        pygame.draw.rect(screen, "red", (320, 250, 150,50))
        screen.blit(yesText, (178, 259))
        screen.blit(noText, (373.5, 259))
        pygame.display.flip()

        print(noRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if yesRect.collidepoint(event.pos):
                        plyrStart = True
                    if noRect.collidepoint(event.pos):
                        pygame.quit()

    
    # Start screen button
    start_button = pygame.Rect(200,350,100,100)
    game_start = True

    # Once game has been started by player
    while game_start:

        mouse_pos = pygame.mouse.get_pos()

        ### Pre-game procedures
        board.drawBoard(screen, player_data, x_img, o_img)                

        pygame.display.flip()

        # Check player turn
        if ctr % 2 == 0:
            p1_turn = False
        else:
            p1_turn = True

        if p1_turn:
            plyr = 1
        else:
            plyr = 2

        # Examine events (quit, player choice)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = False # Break out of game logic
                running = False # Break out of pygame instance, end
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if p1_turn == True:
                        if checkSpot(player_data, mouse_pos):
                            continue
                        setSpot(player_data, mouse_pos, 1)
                    else:
                        if checkSpot(player_data, mouse_pos):
                            continue
                        setSpot(player_data, mouse_pos, 2)
                    ctr += 1
                    print(ctr)
                    print(player_data[0])

        # Keep frame rate at 60fps
        clock.tick(60)

        # Check simple win
        if checkWin(player_data, plyr):
            game_start = False
            gameOver = True
            while(gameOver):
                playAgainText = font1.render('Play again?', True, "black", None)
                screen.fill("white")
                screen.blit(playAgainText, (208,150))
                pygame.draw.rect(screen, "green", (130, 250, 150,50))
                pygame.draw.rect(screen, "red", (320, 250, 150,50))
                screen.blit(yesText, (178, 259))
                screen.blit(noText, (373.5, 259))
                pygame.display.flip()
                print(playAgainText.get_rect())

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameOver = False
                        running = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if yesRect.collidepoint(event.pos):
                                player_data = [[0,0,0], [0,0,0], [0,0,0]]
                                ctr = 1
                                game_start = True
                                gameOver = False
                            if noRect.collidepoint(event.pos):
                                pygame.quit()


print(player_data)

pygame.quit()