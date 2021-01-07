import pygame
import os
import time

cross = pygame.image.load(r'C:\Users\justi\OneDrive\Desktop\tictactoe\images\x.png')
circle = pygame.image.load(r'C:\Users\justi\OneDrive\Desktop\tictactoe\images\circle.png')


def grid(screen):
    lines = [[199, 0, 2, 600], [399, 0, 2, 600], [0, 199, 600, 2], [0, 399, 600, 2]]
    for i in range(4):
        rec = pygame.Rect(lines[i][0], lines[i][1], lines[i][2], lines[i][3])
        pygame.draw.rect(screen, (0, 0, 0), rec)


def end(matrix, screen):
    if matrix[0][0] == matrix[0][1] == matrix[0][2] != 0:
        rec = pygame.Rect(70, 90, 500, 2)
        pygame.draw.rect(screen, (255, 0, 0), rec)
    elif matrix[0][0] == matrix[1][0] == matrix[2][0] != 0:
        rec = pygame.Rect(70, 70, 2, 500)
        pygame.draw.rect(screen, (255, 0, 0), rec)
    elif matrix[0][0] == matrix[1][1] == matrix[2][2] != 0:
        rec1 = pygame.Rect(70, 90, 2, 500)
        rec = pygame.transform.rotate(rec1, 45)
        pygame.draw.rect(screen, (255, 0, 0), rec)
    elif matrix[0][2] == matrix[1][2] == matrix[2][2] != 0:
        rec = pygame.Rect(470, 90, 2, 500)
        pygame.draw.rect(screen, (255, 0, 0), rec)
    elif matrix[2][0] == matrix[2][1] == matrix[2][2] != 0:
        rec = pygame.Rect(70, 470, 500, 2)
        pygame.draw.rect(screen, (255, 0, 0), rec)
    elif matrix[2][0] == matrix[1][1] == matrix[0][2] != 0:
        rec1 = pygame.Rect(70, 470, 2, 500)
    elif matrix[0][1] == matrix[1][1] == matrix[2][1] != 0:
        rec = pygame.Rect(270, 00, 2, 500)
        pygame.draw.rect(screen, (255, 0, 0), rec)
    elif matrix[1][0] == matrix[1][1] == matrix[1][2] != 0:
        rec = pygame.Rect(70, 270, 500, 2)
        pygame.draw.rect(screen, (255, 0, 0), rec)
    else:
        return False
    return True


def tictactoe():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (40, 40)
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    global matrix
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    turn = 1  # 1 or 2
    while True:
        pygame.init()
        screen.fill((255, 255, 255))
        grid(screen)
        index = 0
        for i in matrix:
            if i[0] != 0:
                screen.blit(cross, (70, index + 70)) if i[0] == 1 else screen.blit(circle, (70, index + 70))
            if i[1] != 0:
                screen.blit(cross, (270, index + 70)) if i[1] == 1 else screen.blit(circle, (270, index + 70))
            if i[2] != 0:
                screen.blit(cross, (470, index + 70)) if i[2] == 1 else screen.blit(circle, (470, index + 70))
            index += 200

        if end(matrix, screen) == True:
            pygame.display.update()
            time.sleep(2)
            pygame.display.quit()
            return False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x < 200 and y < 200:
                    matrix[0][0] = turn
                elif x < 200 and y < 400:
                    matrix[1][0] = turn
                elif x < 200 and y < 600:
                    matrix[2][0] = turn
                elif x < 400 and y < 200:
                    matrix[0][1] = turn
                elif x < 400 and y < 400:
                    matrix[1][1] = turn
                elif x < 400 and y < 600:
                    matrix[2][1] = turn
                elif x < 600 and y < 200:
                    matrix[0][2] = turn
                elif x < 600 and y < 400:
                    matrix[1][2] = turn
                elif x < 600 and y < 600:
                    matrix[2][2] = turn
                else:
                    pass
                if turn == 1:
                    turn += 1
                else:
                    turn -= 1

        pygame.display.update()


if __name__ == "__main__":
    tictactoe()
