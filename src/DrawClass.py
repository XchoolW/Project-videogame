import pygame
import os

# Getting the current directory
current_dir = os.path.dirname(__file__)

# Setting the Background, width and height
BACKGROUND = pygame.image.load(os.path.join(
    current_dir, 'img', 'background.png'))

WIDTH, HEIGHT = 800, 600

# Drawing class

class Drawing():

    # Constructor
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.SysFont('comicsans', 50)

    # Drawing method
    def drawing(self, game, player, enemies, gifts, FPS, score): #FPS method was removed
        self.window.blit(BACKGROUND, (0, 0))
        player.fire(self.window)

        # Drawing the gift
        for gift in gifts:
            gift.draw(self.window)

        for enemy in enemies[:]:  # This generate a copy of the list
            enemy.draw(self.window)

        player.draw(self.window)

        # Drawing the HUD and updating the screen
        game.draw_HUD()
        pygame.display.update()

        # Drawing the label for the total points in a game
        points_label = self.font.render(f'Points: {score}', 1, (255, 255, 255))
        self.window.blit(points_label, (HEIGHT/2, 10))
