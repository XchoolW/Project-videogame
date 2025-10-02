import pygame
import random
from ShipClass import Ship

WIDTH = 800
HEIGHT = 600

# List of possible gift images (images are loaded once at the beginning)
GIFT_IMAGES = [
    pygame.image.load('src/img/shot_purple.png'),
    pygame.image.load('src/img/shot_green.png'),
    pygame.image.load('src/img/shot_blue.png')
]

# Class for the gifts


class Gift():
    def __init__(self, x, y, img, speed=10):
        self.x = x
        self.y = y
        self.img = img
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.img)

    # Moving the gifts
    def move(self):
        self.y += self.speed  # Move the gift downward

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))  # Draw the gift image

    def collision(self, obj):
        # Check for collisions with the player or other objects
        offset = (int(obj.x - self.x), int(obj.y - self.y))
        return self.mask.overlap(obj.mask, offset)

    # Creating a static method to avoid use parameters
    @staticmethod
    def create():
        # Randomly select a gift image from the pre-loaded list
        img = random.choice(GIFT_IMAGES)
        x = random.randint(20, WIDTH - 20)
        y = random.randint(-1000, -100)
        return Gift(x, y, img)
