# Tic Tac Toe Game

import pygame

player_data = [[' '] * 3] * 3
test_data = [[1,0,0], [0,1,0], [0,0,1]]

print(player_data)
print(test_data)
pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
running = True

pt1 = pygame.Rect(0,0,200,200)
pt2 = pygame.Rect(200,0,200,200)
pt3 = pygame.Rect(400,0,200,200)
pt4 = pygame.Rect(0,200,200,200)
pt5 = pygame.Rect(200,200,200,200)
pt6 = pygame.Rect(400,200,200,200)
pt7 = pygame.Rect(0,400,200,200)
pt8 = pygame.Rect(200,400,200,200)
pt9 = pygame.Rect(400,400,200,200)

while running:

    ### Pre-game procedures

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("gray")

    pygame.draw.rect(screen, "red", [0,0,200,200])
    pygame.draw.rect(screen, "blue", [200,0,200,200])
    pygame.draw.rect(screen, "orange", [400,0,200,200])
    pygame.draw.rect(screen, "red", [0,200,200,200])
    pygame.draw.rect(screen, "blue", [200,200,200,200])
    pygame.draw.rect(screen, "orange", [400,200,200,200])
    pygame.draw.rect(screen, "red", [0,400,200,200])
    pygame.draw.rect(screen, "blue", [200,400,200,200])
    pygame.draw.rect(screen, "orange", [400,400,200,200])

    # vertical lines
    pygame.draw.line(screen, "black", (200, 0), (200, 600), width=12)
    pygame.draw.line(screen, "black", (400, 0), (400, 600), width=12)
    
    # horizontal lines
    pygame.draw.line(screen, "black", (0, 200), (600, 200), width=12)
    pygame.draw.line(screen, "black", (0, 400), (600, 400), width=12)

    pygame.display.flip()

    ### Game start

    game_result = False
    i = 0

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1 and pt1.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "red", (323,34,144,144))
            pygame.display.flip()
            i += 1
            game_result = True

    clock.tick(60)

pygame.quit()