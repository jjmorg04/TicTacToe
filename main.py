# Tic Tac Toe Game
import pygame
from board import Board
from events import checkSpot, setSpot

# Player data on game start -> all empty
player_data = [[0,0,0], [0,0,0], [0,0,0]]
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

        # Examine events (quit, player choice)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = False
                running = False
    
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
        if player_data[0] == [1, 1, 1]:
            game_start = False
            running = False # Remove and replace with game over screen

print(player_data)

pygame.quit()