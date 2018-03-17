import pygame
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

display_width = 800
display_height = 800

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("TicTacToe")

font = pygame.font.SysFont(None, 100)

posM_x = 250
posM_y = 250

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [250, 250])

def remis():
    font = pygame.font.SysFont(None, 50)
    gameDisplay.fill(green)
    screen_text = font.render("Remis!", True, black)
    gameDisplay.blit(screen_text, [300, 400])
    pygame.display.update()
    time.sleep(2)
    gameLoop()

def wygranaX():
    font = pygame.font.SysFont(None, 50)
    gameDisplay.fill(red)
    screen_text = font.render("Wygral krzyzyk!", True, black)
    gameDisplay.blit(screen_text, [300, 400])
    pygame.display.update()
    time.sleep(2)
    gameLoop()

def wygranaO():
    font = pygame.font.SysFont(None, 50)
    gameDisplay.fill(blue)
    screen_text = font.render("Wygralo kolko!", True, black)
    gameDisplay.blit(screen_text, [300, 400])
    pygame.display.update()
    time.sleep(2)
    gameLoop()

def gameLoop():

    gameExit = False

    pos_x = 0
    pos_y = 250
    x = 0

    X1 = -200
    XX1 = -200
    X2 = -200
    XX2 = -200
    X3 = -200
    XX3 = -200
    X4 = -200
    XX4 = -200
    X5 = -200
    XX5 = -200

    O1 = -200
    OO1 = -200
    O2 = -200
    OO2 = -200
    O3 = -200
    OO3 = -200
    O4 = -200
    OO4 = -200

    pozycja = 1

    win_X1 = 0
    win_X2 = 0
    win_X3 = 0
    win_X4 = 0
    win_X5 = 0

    win_O1 = 0
    win_O2 = 0
    win_O3 = 0
    win_O4 = 0

    font = pygame.font.SysFont(None, 200)

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pos_x -= 270
                    pozycja -= 1
                elif event.key == pygame.K_RIGHT:
                    pos_x += 270
                    pozycja += 1
                elif event.key == pygame.K_UP:
                    pos_y -= 270
                    pozycja -= 3
                elif event.key == pygame.K_DOWN:
                    pos_y += 270
                    pozycja += 3
                elif event.key == pygame.K_SPACE:
                    x += 5

#WYGRANA X

        if win_X1 == 1 or win_X2 == 1 or win_X3 == 1 or win_X4 == 1 or win_X5 == 1:
            if win_X1 == 2 or win_X2 == 2 or win_X3 == 2 or win_X4 == 2 or win_X5 == 2:
                if win_X1 == 3 or win_X2 == 3 or win_X3 == 3 or win_X4 == 3 or win_X5 == 3:
                    wygranaX()
            if win_X1 == 4 or win_X2 == 4 or win_X3 == 4 or win_X4 == 4 or win_X5 == 4:
                if win_X1 == 7 or win_X2 == 7 or win_X3 == 7 or win_X4 == 7 or win_X5 == 7:
                    wygranaX()
            if win_X1 == 5 or win_X2 == 5 or win_X3 == 5 or win_X4 == 5 or win_X5 == 5:
                if win_X1 == 9 or win_X2 == 9 or win_X3 == 9 or win_X4 == 9 or win_X5 == 9:
                    wygranaX()
        if win_X1 == 2 or win_X2 == 2 or win_X3 == 2 or win_X4 == 2 or win_X5 == 2:
            if win_X1 == 5 or win_X2 == 5 or win_X3 == 5 or win_X4 == 5 or win_X5 == 5:
                if win_X1 == 8 or win_X2 == 8 or win_X3 == 8 or win_X4 == 8 or win_X5 == 8:
                    wygranaX()
        if win_X1 == 3 or win_X2 == 3 or win_X3 == 3 or win_X4 == 3 or win_X5 == 3:
            if win_X1 == 6 or win_X2 == 6 or win_X3 == 6 or win_X4 == 6 or win_X5 == 6:
                if win_X1 == 9 or win_X2 == 9 or win_X3 == 9 or win_X4 == 9 or win_X5 == 9:
                    wygranaX()
            if win_X1 == 5 or win_X2 == 5 or win_X3 == 5 or win_X4 == 5 or win_X5 == 5:
                if win_X1 == 7 or win_X2 == 7 or win_X3 == 7 or win_X4 == 7 or win_X5 == 7:
                    wygranaX()
        if win_X1 == 4 or win_X2 == 4 or win_X3 == 4 or win_X4 == 4 or win_X5 == 4:
            if win_X1 == 5 or win_X2 == 5 or win_X3 == 5 or win_X4 == 5 or win_X5 == 5:
                if win_X1 == 6 or win_X2 == 6 or win_X3 == 6 or win_X4 == 6 or win_X5 == 6:
                    wygranaX()
        if win_X1 == 7 or win_X2 == 7 or win_X3 == 7 or win_X4 == 7 or win_X5 == 7:
            if win_X1 == 8 or win_X2 == 8 or win_X3 == 8 or win_X4 == 8 or win_X5 == 8:
                if win_X1 == 9 or win_X2 == 9 or win_X3 == 9 or win_X4 == 9 or win_X5 == 9:
                    wygranaX()

#WYGRANA O

        if win_O1 == 1 or win_O2 == 1 or win_O3 == 1 or win_O4 == 1:
            if win_O1 == 2 or win_O2 == 2 or win_O3 == 2 or win_O4 == 2:
                if win_O1 == 3 or win_O2 == 3 or win_O3 == 3 or win_O4 == 3:
                    wygranaO()
            if win_O1 == 4 or win_O2 == 4 or win_O3 == 4 or win_O4 == 4:
                if win_O1 == 7 or win_O2 == 7 or win_O3 == 7 or win_O4 == 7:
                    wygranaO()
            if win_O1 == 5 or win_O2 == 5 or win_O3 == 5 or win_O4 == 5:
                if win_O1 == 9 or win_O2 == 9 or win_O3 == 9 or win_O4 == 9:
                    wygranaO()
        if win_O1 == 2 or win_O2 == 2 or win_O3 == 2 or win_O4 == 2:
            if win_O1 == 5 or win_O2 == 5 or win_O3 == 5 or win_O4 == 5:
                if win_O1 == 8 or win_O2 == 8 or win_O3 == 8 or win_O4 == 8:
                    wygranaO()
        if win_O1 == 3 or win_O2 == 3 or win_O3 == 3 or win_O4 == 3:
            if win_O1 == 6 or win_O2 == 6 or win_O3 == 6 or win_O4 == 6:
                if win_O1 == 9 or win_O2 == 9 or win_O3 == 9 or win_O4 == 9:
                    wygranaO()
            if win_O1 == 5 or win_O2 == 5 or win_O3 == 5 or win_O4 == 5:
                if win_O1 == 7 or win_O2 == 7 or win_O3 == 7 or win_O4 == 7:
                    wygranaO()
        if win_O1 == 4 or win_O2 == 4 or win_O3 == 4 or win_O4 == 4:
            if win_O1 == 5 or win_O2 == 5 or win_O3 == 5 or win_O4 == 5:
                if win_O1 == 6 or win_O2 == 6 or win_O3 == 6 or win_O4 == 6:
                    wygranaO()
        if win_O1 == 7 or win_O2 == 7 or win_O3 == 7 or win_O4 == 7:
            if win_O1 == 8 or win_O2 == 8 or win_O3 == 8 or win_O4 == 8:
                if win_O1 == 9 or win_O2 == 9 or win_O3 == 9 or win_O4 == 9:
                    wygranaO()



        if x == 5:
            win_X1 += pozycja
            x += 5
            X1 = X1 + 275 + pos_x
            XX1 = XX1 + 25 + pos_y
        elif x == 15:
            win_O1 += pozycja
            x += 5
            O1 = O1 + 275 + pos_x
            OO1 = OO1 + 25 + pos_y
        elif x == 25:
            win_X2 += pozycja
            x += 5
            X2 = X2 + 275 + pos_x
            XX2 = XX2 + 25 + pos_y
        elif x == 35:
            win_O2 += pozycja
            x += 5
            O2 = O2 + 275 + pos_x
            OO2 = OO2 + 25 + pos_y
        elif x == 45:
            win_X3 += pozycja
            x += 5
            X3 = X3 + 275 + pos_x
            XX3 = XX3 + 25 + pos_y
        elif x == 55:
            win_O3 += pozycja
            x += 5
            O3 = O3 + 275 + pos_x
            OO3 = OO3 + 25 + pos_y
        elif x == 65:
            win_X4 += pozycja
            x += 5
            X4 = X4 + 275 + pos_x
            XX4 = XX4 + 25 + pos_y
        elif x == 75:
            win_O4 += pozycja
            x += 5
            O4 = O4 + 275 + pos_x
            OO4 = OO4 + 25 + pos_y
        elif x == 85:
            win_X5 += pozycja
            x += 5
            X5 = X5 + 275 + pos_x
            XX5 = XX5 + 25 + pos_y
        elif x == 90:
            remis()



        if pos_x < 0:
            pos_x += 270
        elif pos_x > 800:
            pos_x -= 270
        elif pos_y < 0:
            pos_y += 270
        elif pos_y > 800:
            pos_y -= 270


        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, black, [260, 0, 10, 800])
        pygame.draw.rect(gameDisplay, black, [530, 0, 10, 800])
        pygame.draw.rect(gameDisplay, black, [0, 260, 800, 10])
        pygame.draw.rect(gameDisplay, black, [0, 530, 800, 10])
        pygame.draw.rect(gameDisplay, red, [pos_x, pos_y, 260, 10])
        screen_text = font.render("X", True, red)
        gameDisplay.blit(screen_text, (X1, XX1))
        screen_text = font.render("O", True, blue)
        gameDisplay.blit(screen_text, [O1, OO1])
        screen_text = font.render("X", True, red)
        gameDisplay.blit(screen_text, [X2, XX2])
        screen_text = font.render("O", True, blue)
        gameDisplay.blit(screen_text, [O2, OO2])
        screen_text = font.render("X", True, red)
        gameDisplay.blit(screen_text, [X3, XX3])
        screen_text = font.render("O", True, blue)
        gameDisplay.blit(screen_text, [O3, OO3])
        screen_text = font.render("X", True, red)
        gameDisplay.blit(screen_text, [X4, XX4])
        screen_text = font.render("O", True, blue)
        gameDisplay.blit(screen_text, [O4, OO4])
        screen_text = font.render("X", True, red)
        gameDisplay.blit(screen_text, [X5, XX5])

        pygame.display.update()

    pygame.quit()
    quit()

gameLoop()

