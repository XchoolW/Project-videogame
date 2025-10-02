import pygame
import os

# Getting the current directory
current_dir = os.path.dirname(__file__)

# Bullet image for the spaceship
BULLET_IMAGE = pygame.image.load(os.path.join(
    current_dir, 'img', 'bullet_image.png'))

# Creating the class that will control the game


class Game():

    # Constructor with all the parameters that we need
    def __init__(self, font, FPS, lives, health, window, screen_width, screen_height, bullets=0, clock=pygame.time.Clock()):
        self.font = font
        self.HEIGHT = screen_height
        self.WIDTH = screen_width
        self.FPS = FPS
        self.lives = lives
        self.level = 1
        self.count = 0
        self.window = window
        self.clock = clock
        self.bullets = bullets
        self.bullet_img = BULLET_IMAGE
        self.health = health

        # Max punctuation
        logs = self.read_logs('scores.txt')
        if len(logs) > 0:
            self.player, self.max_score = logs[0]
        else:
            self.max_score = 0

    # Detect if the player lose.
    def over(self):
        if self.lives <= 0:
            self.count = 0

            while True:
                self.clock.tick(self.FPS)  # Activating pygame clock

                # Creating the label for GAME OVER
                lost_label = self.font.render('GAME OVER', 1, (255, 255, 255))

                # For easy reading, creating coordinates
                x = (self.WIDTH-lost_label.get_width())/2
                y = (self.HEIGHT-lost_label.get_height())/2

                # Draw the label on the specify coordinates
                self.window.blit(lost_label, (x, y))

                # Updating screen
                pygame.display.update()

                # Time that label will appear on the screen
                self.count += 1
                if self.count == self.FPS*4:
                    break

            # Return True because we lost
            return True
        else:
            # Return False because we have not lost
            return False

    def draw_HUD(self):
        # Distance between the bullets
        offset = 0

        # Creating the labels for lives and the level.
        lives_label = self.font.render(
            f'Lives: {self.lives}', 1, (255, 255, 255))
        level_label = self.font.render(
            f'Level: {self.level}', 1, (255, 255, 255))

        # Creating label for health
        health_label = self.font.render(
            f'Health: {self.health}', 1, (255, 160, 160))

        x = (self.WIDTH-level_label.get_width()-10)  # Same technique as before
        y = 10

        # Drawing on the screen
        self.window.blit(lives_label, (10, 10))
        self.window.blit(level_label, (x, y))
        self.window.blit(health_label, (30, self.HEIGHT - 60))

        # Drawing the bullets
        for i in range(self.bullets):
            offset += self.bullet_img.get_width()
            self.window.blit(
                self.bullet_img, (self.WIDTH-offset, self.HEIGHT-50)
            )

    def reload_bullet(self, bullet):
        self.bullets = bullet

    # Method that will work when we wanted to exit the game
    def escape(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            else:
                return False

    # Reading the information for the scores
    def read_logs(self, filename):
        logs = []

        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, score = line.strip().split(',')
                    logs.append((name, int(score)))
                    print(score)
        except FileNotFoundError:
            print('File does not exits')

        logs_sorted = sorted(logs, key=lambda x: x[1], reverse=True)[:5]
        return logs_sorted
