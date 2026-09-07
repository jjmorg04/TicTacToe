# Tic Tac Toe Game

import pygame

player_data = [[0,0,0], [0,0,0], [0,0,0]]
test_data = [[1,0,0], [0,1,0], [0,0,1]]

pygame.display.set_caption("Tic Tac Toe!")

print(player_data)
print(test_data)
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
running = True

p1_turn = True

x_img = pygame.image.load('X.png').convert()
o_img = pygame.image.load('O.png').convert()

pt1 = pygame.Rect(0,0,200,200)
pt2 = pygame.Rect(200,0,200,200)
pt3 = pygame.Rect(400,0,200,200)
pt4 = pygame.Rect(0,200,200,200)
pt5 = pygame.Rect(200,200,200,200)
pt6 = pygame.Rect(400,200,200,200)
pt7 = pygame.Rect(0,400,200,200)
pt8 = pygame.Rect(200,400,200,200)
pt9 = pygame.Rect(400,400,200,200)

ctr = 1

game_start = False

while running:

    start_button = pygame.Rect(200,350,100,100)
    game_start = True

    while game_start:

        ### Pre-game procedures

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")

        # vertical lines
        pygame.draw.line(screen, "black", (200, 0), (200, 600), width=12)
        pygame.draw.line(screen, "black", (398, 0), (398, 600), width=12)
        
        # horizontal lines
        pygame.draw.line(screen, "black", (0, 200), (600, 200), width=12)
        pygame.draw.line(screen, "black", (0, 398), (600, 398), width=12)

        for i in range(len(player_data)):
            for j in range(len(player_data)):
                if player_data[i][j] == 1:
                    screen.blit(x_img, (j * 200, i * 200))
                elif player_data[i][j] == 2:
                    screen.blit(o_img, (j * 200, i * 200))
                
        # vertical lines
        pygame.draw.line(screen, "black", (200, 0), (200, 600), width=12)
        pygame.draw.line(screen, "black", (398, 0), (398, 600), width=12)
        
        # horizontal lines
        pygame.draw.line(screen, "black", (0, 200), (600, 200), width=12)
        pygame.draw.line(screen, "black", (0, 398), (600, 398), width=12)
        pygame.draw.rect(screen, "red", (200, 350, 400, 100))
                

        pygame.display.flip()

        if ctr % 2 == 0:
            p1_turn = False
        else:
            p1_turn = True

        ### Game start

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if p1_turn == True:
                    if player_data[mouse_pos[1] // 200][mouse_pos[0] // 200] == 1 or player_data[mouse_pos[1] // 200][mouse_pos[0] // 200] == 2:
                        continue
                    player_data[mouse_pos[1] // 200][mouse_pos[0] // 200] = 1
                else:
                    if player_data[mouse_pos[1] // 200][mouse_pos[0] // 200] == 1 or player_data[mouse_pos[1] // 200][mouse_pos[0] // 200] == 2:
                        continue
                    player_data[mouse_pos[1] // 200][mouse_pos[0] // 200] = 2
                ctr += 1
                print(ctr)
                print(player_data[0])


        clock.tick(60)

        if player_data[0] == [1, 1, 1]:
            game_start = False

print(player_data)

pygame.quit()