import pygame
# Commented out code is there to change the display of the game to the original


class Paddle(pygame.sprite.Sprite):

    def __init__(self, main_surface, color, width, height):
        super().__init__()
        self.main_surface = main_surface
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.image.load("milkyway.png")
        # self.image = pygame.Surface((width, height))
        # Get the rect coordinates
        self.rect = self.image.get_rect()
        # self.image.fill(color)

    def move(self, position):
        """
        This function makes the x coordinates of the paddle able to move
        :param position: the coordinates of the mouse
        :return: nothing
        """
        self.rect.x = position[0]
