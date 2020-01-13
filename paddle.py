import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, main_surface, color, width, height):
        super().__init__()
        # initialize sprite super class

        # finish setting the class variables to the parameters
        self.main_surface = main_surface
        self.color = color
        self.width = width
        self.height = height

        # Create a surface with the correct height and width
        self.image = pygame.Surface((width, height))

        # Get the rect coordinates
        self.rect = self.image.get_rect()

        # Fill the surface with the correct color
        self.image.fill(color)

    # Track the x coordinate, don't let it move off the screen
    def move(self, position):
        self.rect.x = position[0]

