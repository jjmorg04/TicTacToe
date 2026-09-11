import pygame

# Board class
class Board:
    # Function to draw the board every 'flip'
    def drawBoard(self, screen, player_data, x_img, o_img):

        reprint = False

        # Set game background color
        screen.fill("white")

        # Draw the vertical lines
        pygame.draw.line(screen, "black", (200, 0), (200, 600), width=12)
        pygame.draw.line(screen, "black", (398, 0), (398, 600), width=12)
        
        # Draw the horizontal lines
        pygame.draw.line(screen, "black", (0, 200), (600, 200), width=12)
        pygame.draw.line(screen, "black", (0, 398), (600, 398), width=12)

        # For all data points in player_data, print all used grids
        for i in range(len(player_data)):
                    for j in range(len(player_data)):
                        if player_data[i][j] == 1:
                            screen.blit(x_img, (j * 200, i * 200))
                            reprint = True
                        elif player_data[i][j] == 2:
                            screen.blit(o_img, (j * 200, i * 200))
                            reprint = True

        if reprint:
             # Draw the vertical lines
                pygame.draw.line(screen, "black", (200, 0), (200, 600), width=12)
                pygame.draw.line(screen, "black", (398, 0), (398, 600), width=12)
                
                # Draw the horizontal lines
                pygame.draw.line(screen, "black", (0, 200), (600, 200), width=12)
                pygame.draw.line(screen, "black", (0, 398), (600, 398), width=12)