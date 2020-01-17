import pygame
# Commented out code is there to change the display of the game to the original


class Brick(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.image.load("twix.png")
        # self.image = pygame.Surface((width, height))
        # Get the rect coordinates
        self.rect = self.image.get_rect()
        # self.image.fill(color)
