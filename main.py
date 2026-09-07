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

    # vertical lines
    pygame.draw.line(screen, "black", (200, 0), (200, 600), width=12)
    pygame.draw.line(screen, "black", (400, 0), (400, 600), width=12)
    
    # horizontal lines
    pygame.draw.line(screen, "black", (0, 200), (600, 200), width=12)
    pygame.draw.line(screen, "black", (0, 400), (600, 400), width=12)

    for i in range(len(test_data)):
        for j in range(len(test_data)):
            if test_data[i][j] == 1:
                pygame.draw.rect(screen, "red", [i * 200, j * 200, 100, 100])

    pygame.display.flip()


    ### Game start

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            player_data[mouse_pos[1] // 200][mouse_pos[0] // 200] = 1

        for i in range(len(test_data)):
                for j in range(len(test_data)):
                    if test_data[i][j] == 1:
                        pygame.draw.rect(screen, "red", [i * 200, j * 200, 100, 100])
        pygame.display.flip() 


    clock.tick(60)

print(player_data)

pygame.quit()