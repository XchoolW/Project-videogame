import pygame
import os
from ShipClass import Ship
from BulletClass import Bullet
import time

# Getting the current directory
current_dir = os.path.dirname(__file__)

# Constants for the Images
PLAYER_IMAGE = pygame.image.load(os.path.join(
    current_dir, 'img', 'player_image.png'))
PLAYER_IMAGE_DAMAGE = pygame.image.load(os.path.join(
    current_dir, 'img', 'player_image_damage.png'))
BULLET_IMAGE = pygame.image.load(os.path.join(
    current_dir, 'img', 'bullet_image.png'))
WIDTH = 800
HEIGHT = 600

# Creating the class for the player ------------------------------------------------


class Player(Ship): # Inherit from Ship class

    # Constructor
    def __init__(self, x, y, x_speed, y_speed, health=100):
        super().__init__(x, y, health)  # Super constructor

        self.x_speed = x_speed
        self.y_speed = y_speed
        self.ship_img = PLAYER_IMAGE
        self.bullet_img = BULLET_IMAGE
        self.bullet_speed = -10
        self.max_health = health
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.creation_cooldown_counter = 0
        self.max_amount_bullets = 3
        self.bullets = []
        self.bullet_cooldown_counter = 0
        self.last_hit_time = 0
        self.ship_img_damage = PLAYER_IMAGE_DAMAGE
        self.ship_change_time = 0  # Store time when the ship is changed
        self.ship_duration = 1

    # Method for movement
    def move(self):
        keys = pygame.key.get_pressed()

        # Moving up
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and (self.y > 0):
            self.y -= self.y_speed

        # Moving down
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (self.y < HEIGHT - self.ship_img.get_height()-20):
            self.y += self.y_speed

        # Moving right
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (self.x < WIDTH - self.ship_img.get_width()):
            self.x += self.x_speed

        # Moving left
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (self.x > 0):
            self.x -= self.x_speed

    # Increasing speed and limit the speed
    def increase_speed(self):
        if self.x_speed < 10:
            self.x_speed += 1.25
            self.y_speed += 1.25
        elif self.x_speed >= 10:
            self.x_speed = 10
            self.y_speed = 8

        # Cooldown for the bullets if the actual cooldown is greater than 25
        if self.cool_down > 25:
            self.cool_down *= 0.9

    # Creating the bullets for our ship
    def create_bullets(self):
        if (len(self.bullets) < self.max_amount_bullets) and (self.creation_cooldown_counter == 0):
            bullet = Bullet(self.x, self.y, self.bullet_img)
            self.bullets.append(bullet)

            self.creation_cooldown_counter = 1

        for bullet in self.fired_bullets:
            if bullet.y <= -40:
                self.fired_bullets.pop(0)

    # Method for the cooldown in the bullets
    def cooldown(self):
        # Cooldown for fire
        if self.bullet_cooldown_counter >= 20:
            self.bullet_cooldown_counter = 0
        elif self.bullet_cooldown_counter > 0:
            self.bullet_cooldown_counter += 1

        # Cooldown for creating bullets
        if self.creation_cooldown_counter >= self.cool_down:
            self.creation_cooldown_counter = 0
        elif self.creation_cooldown_counter > 0:
            self.creation_cooldown_counter += 1

    # Method for fire the proyectiles
    def fire(self, window):

        # Setting the key for shooting -------------------------------------------------
        keys = pygame.key.get_pressed()

        # Analyze if the ship has pressed space, has bullets and cooldown is 0
        if (keys[pygame.K_SPACE]) and (len(self.bullets) > 0) and (self.bullet_cooldown_counter == 0):

            # Placing the bullet in the middle of the ship
            self.bullets[-1].x = self.x + \
                (self.ship_img.get_width() - self.bullet_img.get_width())/2

            # Placing the bullet a little bit upper
            self.bullets[-1].y = self.y + 10

            # Take the last bullet on the list and add it to firebullets list
            self.fired_bullets.append(self.bullets.pop())

            # Start the cooldown
            self.bullet_cooldown_counter = 1
            self.creation_cooldown_counter = 1

        # Moving the fired bullets
        for i in range(len(self.fired_bullets)):
            self.fired_bullets[i].move(self.bullet_speed)
            self.fired_bullets[i].draw(window)

    # Method to detect if you hit the enemy
    def hit(self, enemy):

        for i in range(len(self.fired_bullets)):

            # If you hit the enemy, your cooldown get lower
            self.creation_cooldown_counter = self.cool_down * 0.8

            # Detecting collision
            return self.fired_bullets[i].collision(enemy)

    # Function to take damage if we crashed with the enemy
    def take_damage(self, damage, cooldown_time=1000):

        # Cheking the current time
        current_time = pygame.time.get_ticks()

        # Cheking if the enogh time has passed since the last damage
        if current_time - self.last_hit_time >= cooldown_time:
            self.health -= damage
            self.last_hit_time = current_time

            self.ship_img = self.ship_img_damage  # Change the ship image

            # Set the time when the ship image changes
            self.ship_change_time = time.time()

    # Update the player ship
    def update(self):
        # Check if 1 second has passed and revert the ship image
        if time.time() - self.ship_change_time >= self.ship_duration:
            self.ship_img = PLAYER_IMAGE  # Revert to the original image
