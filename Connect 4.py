import pygame

NONE = 0
RED = 1
YELLOW = 2

HORIZONTAL = 0
VERTICAL = 1

GRID_SIZE = (7, 6)
WIN_NUMBER = 4

screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

coloums = [[]] * GRID_SIZE[0]
round = False

for i in range(GRID_SIZE[0]):
    coloums[i] = [0] * GRID_SIZE[1]

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                for i in range(GRID_SIZE[0]):
                    if pygame.Rect.collidepoint(pygame.Rect(50 + (i * 100), 50, 100, GRID_SIZE[1] * 100), event.pos):
                        for j in range(GRID_SIZE[1]):
                            if coloums[i][j] == NONE and round == False:
                                coloums[i][j] = RED
                                round = True
                                break
                            elif coloums[i][j] == NONE and round == True:
                                coloums[i][j] = YELLOW
                                round = False
                                break
    
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            pygame.draw.rect(screen, (0, 0, 0), (50 + (i * 100), 550 - (j * 100), 100, 100), 3)
            if coloums[i][j] == RED:
                pygame.draw.rect(screen, (255, 0, 0), (50 + (i * 100), 550 - (j * 100), 100, 100))
            elif coloums[i][j] == YELLOW:
                pygame.draw.rect(screen, (255, 255, 0), (50 + (i * 100), 550 - (j * 100), 100, 100))
            
            horz_win = True
            vert_win = True
            slop_l_win = True
            slop_r_win = True
            win = False
            for k in range(WIN_NUMBER):
                if i < GRID_SIZE[1]-2 and coloums[i][j] != NONE:
                    if coloums[i+k][j] != coloums[i][j]:
                        horz_win = False
                else:
                    horz_win = False
                
                if j < GRID_SIZE[0]-4 and coloums[i][j] != NONE:
                    if coloums[i][j+k] != coloums[i][j]:
                        vert_win = False
                else:
                    vert_win = False

                if j < GRID_SIZE[0]-4 and i < GRID_SIZE[1]+1 and coloums[i][j] != NONE:
                    if i < GRID_SIZE[1]-2:
                        if coloums[i+k][j+k] != coloums[i][j]:
                            slop_r_win = False
                    else:
                        slop_r_win = False

                    if coloums[i-k][j+k] != coloums[i][j]:
                        slop_l_win = False
                else:
                    slop_l_win = False
                    slop_r_win = False

            if horz_win == True or vert_win == True or slop_l_win == True or slop_r_win == True:
                win = True

            if win:
                print(f"Winner is {coloums[i][j]}")
                exit(0)

    pygame.display.flip()
    clock.tick(60)
