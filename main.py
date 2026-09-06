# Tic Tac Toe Game

import pygame

player_data = [[' '] * 3] * 3

print(player_data)
pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
running = True

button1 = pygame.Rect(34,34,144,144)

while running:

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("gray")

    pygame.draw.rect(screen, "red", (34,34,144,144))
    pygame.draw.rect(screen, "blue", (178,34,144,144))

    pygame.draw.line(screen, "black", (180, 34), (180, 466), width=8)
    pygame.draw.line(screen, "black", (34, 320), (466, 320), width=8)
    pygame.draw.line(screen, "black", (34, 180), (466, 180), width=8)
    pygame.draw.line(screen, "black", (320, 34), (320, 466), width=8)

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1 and button1.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "red", (323,34,144,144))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()