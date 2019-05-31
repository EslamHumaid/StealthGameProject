import pygame
import time
pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)

mainCharImg = pygame.image.load('Images/standing.png')
walkRight = [pygame.image.load('Images/r2.png'), pygame.image.load('Images/r3.png'), pygame.image.load('Images/r4.png'), pygame.image.load('Images/r5.png'), pygame.image.load('Images/r6.png'), pygame.image.load('Images/r7.png'), pygame.image.load('Images/r8.png'), pygame.image.load('Images/r9.png')]
walkLeft = [pygame.image.load('Images/l1.png'), pygame.image.load('Images/l2.png'), pygame.image.load('Images/l3.png'), pygame.image.load('Images/l4.png'), pygame.image.load('Images/l5.png'), pygame.image.load('Images/l6.png'), pygame.image.load('Images/l7.png'), pygame.image.load('Images/l8.png')]
walkUp = [pygame.image.load('Images/u1.png'), pygame.image.load('Images/u2.png'), pygame.image.load('Images/u3.png'), pygame.image.load('Images/u4.png'), pygame.image.load('Images/u5.png'), pygame.image.load('Images/u6.png'), pygame.image.load('Images/u7.png'), pygame.image.load('Images/u8.png')]
walkDown = [pygame.image.load('Images/d1.png'), pygame.image.load('Images/d2.png'), pygame.image.load('Images/d3.png'), pygame.image.load('Images/d4.png'), pygame.image.load('Images/d5.png'), pygame.image.load('Images/d6.png'), pygame.image.load('Images/d7.png'), pygame.image.load('Images/d8.png')]

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Stealth Game')
clock = pygame.time.Clock()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


class Robot:
    def __init__(self, thingx, thingy, thingw, thingh, color):
        self.x = thingx
        self.y = thingy
        self.width = thingw
        self.height = thingh
        self.color = color


class Character:
    def __init__(self, charx, chary):
        self.x = charx
        self.y = chary


def dead():
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects('You Died', largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)

    game_loop()


def game_loop():
    game_exit = False
    main_char = Character(550, 200)
    x_change = 0
    y_change = 0
    robots_y = 300
    xinit_point = 400
    yinit_point = 300
    robots_x = 400
    first_robot = Robot(400, 300, 50, 50, red)
    robots_list = [first_robot]
    robots_direction = 2
    left = False
    right = False
    up = False
    down = False
    walkCount = 0


    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    left = True
                    right = False
                    up = False
                    down = False
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                    left = False
                    right = True
                    up = False
                    down = False
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                    left = False
                    right = False
                    up = False
                    down = True
                elif event.key == pygame.K_UP:
                    y_change = -5
                    left = False
                    right = False
                    up = True
                    down = False
                else:
                    left = False
                    right = False
                    up = False
                    down = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    x_change = 0
                    y_change = 0
                    left = False
                    right = False
                    up = False
                    down = False

        main_char.x += x_change
        main_char.y += y_change

        if main_char.x < 0:
            main_char.x = 0
        elif main_char.x > display_width - 50:
            main_char.x = display_width - 50
        elif main_char.y < 0:
            main_char.y = 0
        elif main_char.y > display_height - 50:
            main_char.y = display_height - 50

        gameDisplay.fill(white)
        # gameDisplay.blit(mainCharImg, (main_char.x, main_char.y))
        if walkCount + 1 >= 24:
            walkCount = 0

        if left:
            gameDisplay.blit(walkLeft[walkCount//3], (main_char.x, main_char.y))
            walkCount += 1
        elif right:
            gameDisplay.blit(walkRight[walkCount//3], (main_char.x, main_char.y))
            walkCount += 1
        elif up:
            gameDisplay.blit(walkUp[walkCount//3], (main_char.x, main_char.y))
            walkCount += 1
        elif down:
            gameDisplay.blit(walkDown[walkCount//3], (main_char.x, main_char.y))
            walkCount += 1
        else:
            gameDisplay.blit(mainCharImg, (main_char.x, main_char.y))

        if robots_x >= xinit_point + 100:
            robots_direction = -2
        elif robots_x <= xinit_point - 100:
            robots_direction = 2

        robots_x += robots_direction

        for robot in robots_list:
            robot.y = robots_y
            robot.x = robots_x
            pygame.draw.rect(gameDisplay, robot.color, (robot.x, robot.y, robot.width, robot.height))

        pygame.display.update()
        clock.tick(24)


# ------------------------------------------------
game_loop()
pygame.quit()
quit()
