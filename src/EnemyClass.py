import pygame
import random
import os
from ShipClass import Ship
from BulletClass import Bullet

# Getting the current directory
current_dir = os.path.dirname(__file__)

# Loading all the enemy images
BULLET_IMAGE = pygame.image.load(os.path.join(
    current_dir, 'img', 'bullet_image.png'))
ENEMY_BLUE_IMAGE = pygame.image.load(os.path.join(
    current_dir, 'img', 'enemy_blue_image.png'))
ENEMY_GREEN_IMAGE = pygame.image.load(os.path.join(
    current_dir, 'img', 'enemy_green_image.png'))
ENEMY_PURPLE_IMAGE = pygame.image.load(os.path.join(
    current_dir, 'img', 'enemy_purple_image.png'))

# Window where we'll going to draw the enemies and its width and height
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Build a Enemy class --------------------------------------------------------

class Enemy(Ship): # Inherit from Ship

    # List with enemy colors
    COLOR = {
        'blue': ENEMY_BLUE_IMAGE,
        'green': ENEMY_GREEN_IMAGE,
        'purple': ENEMY_PURPLE_IMAGE
    }

    # Constructor and its parameters
    def __init__(self, speed, x=50, y=50, color='blue', health=100):
        super().__init__(x, y, health)  # Calling the super constructor

        self.ship_img = self.COLOR[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.speed = speed

    # Give movement to the enemies, based on the speed
    def move(self):
        self.y += self.speed

    # Creating the enemies and the amount we prefer
    def create(self, amount):

        enemies = []

        # Creating the enemies and add them to the enemies list
        for i in range(amount):
            enemy = Enemy(

                # Select x coordinate randomly
                x=random.randrange(20, WIDTH-ENEMY_BLUE_IMAGE.get_width()),

                # Select y coordinate randomly
                y=random.randrange(-1000, -100),

                # Select the color randomly
                color=random.choice(['blue', 'green', 'purple']),
                speed=self.speed)
            enemies.append(enemy)

        # The method will return the list of enemies
        return enemies

    # When we get a new level, the speed will increase 2%
    def increase_speed(self):
        self.speed *= 1.01

    def collision(self, obj):

        # Compare the bullet mask with the obj mask to detect collitions
        offset = (
            int(self.x - obj.x - 30),
            int(self.y - obj.y - 30)
        )

        # This will return the point of the collition
        return self.mask.overlap(obj.mask, (offset))
