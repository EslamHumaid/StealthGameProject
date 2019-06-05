import pygame
import time
pygame.init()

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)


# images
mainCharImg = pygame.image.load('Images/standing.png')
walkRight = [pygame.image.load('Images/r2.png'), pygame.image.load('Images/r3.png'), pygame.image.load('Images/r4.png'), pygame.image.load('Images/r5.png'), pygame.image.load('Images/r6.png'), pygame.image.load('Images/r7.png'), pygame.image.load('Images/r8.png'), pygame.image.load('Images/r9.png')]
walkLeft = [pygame.image.load('Images/l1.png'), pygame.image.load('Images/l2.png'), pygame.image.load('Images/l3.png'), pygame.image.load('Images/l4.png'), pygame.image.load('Images/l5.png'), pygame.image.load('Images/l6.png'), pygame.image.load('Images/l7.png'), pygame.image.load('Images/l8.png')]
walkUp = [pygame.image.load('Images/u1.png'), pygame.image.load('Images/u2.png'), pygame.image.load('Images/u3.png'), pygame.image.load('Images/u4.png'), pygame.image.load('Images/u5.png'), pygame.image.load('Images/u6.png'), pygame.image.load('Images/u7.png'), pygame.image.load('Images/u8.png')]
walkDown = [pygame.image.load('Images/d1.png'), pygame.image.load('Images/d2.png'), pygame.image.load('Images/d3.png'), pygame.image.load('Images/d4.png'), pygame.image.load('Images/d5.png'), pygame.image.load('Images/d6.png'), pygame.image.load('Images/d7.png'), pygame.image.load('Images/d8.png')]
RobotWalkLeft = [pygame.image.load('Images/rl2.png'), pygame.image.load('Images/rl3.png'), pygame.image.load('Images/rl4.png'), pygame.image.load('Images/rl5.png'), pygame.image.load('Images/rl6.png'), pygame.image.load('Images/rl7.png'), pygame.image.load('Images/rl8.png'), pygame.image.load('Images/rl9.png')]
RobotWalkRight = [pygame.image.load('Images/rr1.png'), pygame.image.load('Images/rr2.png'), pygame.image.load('Images/rr3.png'), pygame.image.load('Images/rr4.png'), pygame.image.load('Images/rr5.png'), pygame.image.load('Images/rr6.png'), pygame.image.load('Images/rr7.png'), pygame.image.load('Images/rr8.png')]
game_map = pygame.image.load('Images/map.png')
walls = pygame.image.load('Images/wall.png')
blockImg = pygame.image.load('Images/block.png')
bushImg = pygame.image.load('Images/bush.png')

# display
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Stealth Game')
clock = pygame.time.Clock()


def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


class Robot:
    def __init__(self, thingx, thingy, thingw, thingh):
        self.x = thingx
        self.y = thingy
        self.width = thingw
        self.height = thingh


class Bush:
    def __init__(self, bushx, bushy, bushw, bushh):
        self.x = bushx
        self.y = bushy
        self.width = bushw
        self.height = bushh


class Character:
    def __init__(self, charx, chary, charw, charh):
        self.x = charx
        self.y = chary
        self.width = charw
        self.height = charh


class Block:
    def __init__(self, blockx, blocky, blockw, blockh, blocktype):
        self.x = blockx
        self.y = blocky
        self.width = blockw
        self.height = blockh
        self.type = blocktype


def detected():
    largeText = pygame.font.Font('freesansbold.ttf', 60)
    TextSurf, TextRect = text_objects('You have been detected!!', largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)

    game_loop()


def game_loop():
    game_exit = False
    main_char = Character(550, 200, 30, 49)
    x_change = 0
    y_change = 0
    xinit_point = 400

    first_robot = Robot(400, 300, 33, 47)
    robots_list = [first_robot]
    first_bush = Bush(550, 280, 70, 70)
    bushs_list = [first_bush]
    robots_direction = 2
    first_block = Block(200, 250, 100, 100, 'horizental')
    blocks_list = [first_block]

    left = False
    right = False
    up = False
    down = False
    robot_left = False
    robot_right = True
    hiding = False
    walkCount = 0
    robot_walk_count = 0

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
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                    left = False
                    right = False
                    up = False
                    down = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
                    left = False
                    right = False
                    up = False
                    down = False

        main_char.x += x_change
        main_char.y += y_change

        # boundries
        if main_char.x < 0:
            main_char.x = 0
        elif main_char.x > display_width - 50:
            main_char.x = display_width - 50
        elif main_char.y < 150:
            main_char.y = 150
        elif main_char.y > 450 - 50:
            main_char.y = 450 - 50

        # DRAWING
        gameDisplay.blit(game_map, (0, 150))
        gameDisplay.blit(walls, (0, 130))
        gameDisplay.blit(walls, (0, 450))

        if walkCount + 1 >= 24:
            walkCount = 0

        if robot_walk_count + 1 >= 24:
            robot_walk_count = 0

        # drawing main character
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

        # drawing robots
        for robot in robots_list:

            if robot_left:
                gameDisplay.blit(RobotWalkLeft[robot_walk_count//3], (robot.x, robot.y))
                robot_walk_count += 1
            elif robot_right:
                gameDisplay.blit(RobotWalkRight[robot_walk_count//3], (robot.x, robot.y))
                robot_walk_count += 1

        # drawing blocks
        for block in blocks_list:
            gameDisplay.blit(blockImg, (block.x, block.y))

        # drawing bushs
        for bush in bushs_list:

            gameDisplay.blit(bushImg, (bush.x, bush.y))

        # hiding
        for bush in bushs_list:
            if (main_char.x > bush.x) and (main_char.x < bush.x + bush.width) and (main_char.y > bush.y) and (main_char.y < bush.y + bush.height):

                hiding = True
            else:
                hiding = False

        # detection
        for robot in robots_list:
            if (main_char.x > robot.x - 70) and (main_char.x < robot.x + robot.width + 70) and (not hiding):
                if(main_char.y > robot.y - 50) and (main_char.y < robot.y + robot.height + 50):
                    detected()

        # moving robot
        if first_robot.x >= xinit_point + 100:
            robots_direction = -2
            robot_left = True
            robot_right = False
        elif first_robot.x <= xinit_point - 100:
            robots_direction = 2
            robot_right = True
            robot_left = False

        first_robot.x += robots_direction

        # colliding with blocks
        for block in blocks_list:
            if (main_char.x + main_char.width > block.x) and (main_char.x < block.x + block.width):
                if main_char.y + main_char.height > block.y and main_char.y < block.y + block.height:
                    if down:
                        main_char.y = block.y - main_char.height
                    elif up:
                        main_char.y = block.y + block.height
                    elif right:
                        main_char.x = block.x - main_char.width
                    elif left:
                        main_char.x = block.x + block.width

        pygame.display.update()
        clock.tick(24)


# ------------------------------------------------
game_loop()
pygame.quit()
quit()
