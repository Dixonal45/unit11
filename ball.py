import pygame
# Commented out code is there to change the display of the game to the original


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, window_width, window_height, radius):
        super().__init__()
        self.color = color
        self.window_width = window_width
        self.window_height = window_height
        self.radius = radius
        self.sound = pygame.mixer.Sound('Bite+2.wav')
        # self.image = pygame.Surface((radius, radius))
        # self.image.fill((255, 255, 255))
        self.image = pygame.image.load("ariana.png")
        self.rect = self.image.get_rect()
        # pygame.draw.circle(self.image, (0, 0, 0), (5, 5), 5, 0)
        # Add a circle to represent the ball to the surface just created.
        self.x_speed = 5
        self.y_speed = 6

    def move(self):
        """
        This function says that if the ball hits the sides of the screen, the direction will change
        :return: nothing
        """
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.left < 0 or self.rect.right > self.window_width:
            self.x_speed = -self.x_speed
        if self.rect.top < 0 or self.rect.bottom > self.window_height:
            self.y_speed = -self.y_speed

    def collide(self, sprite_group):
        """
        This function makes it so that if the ball hits a sprite group, the direction of the ball will change
        (used with the paddle in breakout)
        :param sprite_group: A sprite group (the paddle)
        :return: nothing
        """
        if pygame.sprite.spritecollide(self, sprite_group, False):
            self.y_speed = -self.y_speed

    def collide_brick(self, sprite_group):
        """
        This function makes it so that if the ball hits a sprite group, the sprite group hit will vanish
        and the ball direction will change (used with the bricks)
        :param sprite_group: A sprite group (the brick group)
        :return: nothing
        """
        if pygame.sprite.spritecollide(self, sprite_group, True):
            self.sound.play()
            self.y_speed = -self.y_speed
