import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleer."""

    def __init__(self, ai_game):
        # Initialize an alien and set its starting posiont
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('Images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.recy.y = self.rect.height

        # Store the alien's exact horizontal posiont
        self.x = float(self.rect.x)
