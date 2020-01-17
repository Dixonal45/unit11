# Created by Allison Dixon
# Last modified 1/17/2020
# Breakout Game

import pygame, sys
from pygame.locals import *
import brick
import paddle
import ball

pygame.init()
# Commented out code is there to change the display of the game to the original

# These are sounds to be used in functions game_over and win
cheer = pygame.mixer.Sound('cheer.wav')
boo = pygame.mixer.Sound('boohiss.wav')


def game_over(main_surface):
    """
    This functions shows a game over screen if you lose three times and boos you
    :param main_surface: It will be shown on the main surface
    :return: nothing
    """
    main_surface.fill((0, 0, 0))
    font = pygame.font.SysFont('Comic Sans MS', 50)
    label = font.render('GAME OVER', 1, (255, 255, 255))
    main_surface.blit(label, (100, 250))
    boo.play()
    pygame.display.update()
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()


def win(main_surface):
    """
    This function shows a win screen if you hit all the bricks/twix bars and cheers for you
    :param main_surface: It will be shown on the main surface
    :return: nothing
    """
    main_surface.fill((100, 100, 250))
    font = pygame.font.SysFont('Comic Sans MS', 100)
    label = font.render('YOU WIN!', 1, (255, 255, 255))
    main_surface.blit(label, (40, 250))
    cheer.play()
    pygame.display.update()
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()


def main():
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 30

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    colors = [RED, ORANGE, YELLOW, GREEN, CYAN]
    # These are the brick and paddle sprite groups so that the ball can collide with them
    bricks_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()

    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    # The following lines set the background image
    bg = pygame.image.load("candystore.png")
    main_surface.blit(bg, (0, 0))

    # These loops draw the rows of bricks and color them according to the color list, two rows of each
    x_pos = BRICK_SEP
    y_pos = BRICK_Y_OFFSET
    for color in colors:
        for y in range(2):
            for x in range(BRICKS_PER_ROW):
                my_brick = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, color)
                my_brick.rect.x = x_pos
                my_brick.rect.y = y_pos
                bricks_group.add(my_brick)
                main_surface.blit(my_brick.image, (x_pos, y_pos))
                x_pos = x_pos + BRICK_SEP + BRICK_WIDTH
            y_pos += BRICK_HEIGHT + BRICK_SEP
            x_pos = BRICK_SEP
    # The following lines make the paddle appear of the screen
    my_paddle = paddle.Paddle(main_surface, BLACK, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_group.add(my_paddle)
    my_paddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    main_surface.blit(my_paddle.image, my_paddle.rect)
    # The following lines make the ball appear of the screen
    my_ball = ball.Ball(BLACK, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    my_ball.rect.x = APPLICATION_WIDTH/2
    my_ball.rect.y = APPLICATION_HEIGHT/2
    main_surface.blit(my_ball.image, my_ball.rect)
    # The 'tries' variable keeps track of how many times the user has played
    tries = 0

    while True:
        main_surface.blit(bg, (0, 0))
        for a_brick in bricks_group:
            main_surface.blit(a_brick.image, a_brick.rect)
        # The following lines make the paddle move with the mouse and have the sprite groups collide
        my_paddle.move(pygame.mouse.get_pos())
        main_surface.blit(my_paddle.image, my_paddle.rect)
        main_surface.blit(my_ball.image, my_ball.rect)
        my_ball.move()
        my_ball.collide(paddle_group)
        my_ball.collide_brick(bricks_group)
        burp_sound = pygame.mixer.Sound('Burp+3.wav')
        # This if statement says that if the ball hits the bottom of the screen, the ball will reset to the
        # middle of the screen and a try will be added to the tries variable
        if my_ball.rect.bottom >= APPLICATION_HEIGHT:
            burp_sound.play()
            my_ball.rect.y = APPLICATION_HEIGHT / 2
            tries += 1
        # This if statement says if the user has tried three times, the game over screen will show
        # It is >= 3 because the ball will keep hitting the bottom of the screen, and the game would never end
        if tries >= 3:
            game_over(main_surface)
        # This if statement says if there are no more bricks left, the win screen will show
        if len(bricks_group) == 0:
            win(main_surface)
        pygame.display.update()
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()


main()
