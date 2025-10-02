import pygame
import sys
import os
from pygame import mixer

pygame.init()

# Create the game menu


class MainMenu():

    # Constants for colors and screen
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 15)

    WIDTH = 800
    HEIGHT = 600

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Space Invaders')

    # Image directory
    IMG_DIR = 'src/img'

    # Loading the music
    try:
        mixer.music.load('src/sounds/background_song.mp3')
    except:
        print('Music cannot be displayed')
        pass

    # Playing the music
    try:
        mixer.music.play(-1)
    except:
        pass

    def __init__(self, init_game_mtd, init_score_mtd, init_about_mtd):
        self.init_game_mtd = init_game_mtd
        self.init_score_mtd = init_score_mtd
        self.init_about_mtd = init_about_mtd

    # Method to load the image
    def load_img(self, filename):
        path = os.path.join(self.IMG_DIR, filename)

        # Returning on alpha
        return pygame.image.load(path).convert_alpha()

    # Show the text on menu
    def show_text(self, text, font, color, surface, x, y):
        # render the text into object
        text_obj = font.render(text, True, color)
        rect_text = text_obj.get_rect()

        # The way of manipulating the text
        rect_text.center = (x, y)

        # Drawing the text object
        surface.blit(text_obj, rect_text)

        return rect_text

    # Optios for the main menu
    def main_menu(self):

        # options on the menu
        options = ['Play', 'Score', 'About']

        # The option selected by default
        select_option = 0
        selector_rect = pygame.Rect(0, 0, 300, 50)

        # Loading background image
        background = self.load_img('background1.jpg')

        background = pygame.transform.scale(
            background, (self.WIDTH, self.HEIGHT))

        # Loading the hybridge logo
        image = self.load_img('Hybridge.gif')
        image = pygame.transform.scale(image, (80, 80))

        # Menu working
        while True:

            # Drawing the window
            self.WIN.blit(background, (0, 0))

            # Showing the title
            self.show_text('Space Invaders', pygame.font.Font(
                None, 64), self.WHITE, self.WIN, self.WIDTH // 2, self.HEIGHT // 4)

            # Showing the image below the title
            self.WIN.blit(image, (self.WIDTH // 2-40, self.HEIGHT//4 + 60))

            # List of options empty
            text_rectangles = []

            # Drawing the options
            for i, option in enumerate(options):
                rect_text = self.show_text(option, pygame.font.Font(
                    None, 32), self.WHITE, self.WIN, self.WIDTH//2, self.HEIGHT//4 + 90 * (i + 1) + 100)

                text_rectangles.append(rect_text)

            # Drawing the selector
            selector_rect.centerx = self.WIDTH/2
            selector_rect.centery = text_rectangles[select_option].centery

            pygame.draw.rect(self.WIN, self.RED, selector_rect, 2)

            # Updating the screen
            pygame.display.update()

            # Getting events from keyboard
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Logic for the movement and selecting the options
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        select_option = (select_option - 1) % len(options)

                    elif event.key == pygame.K_DOWN:
                        select_option = (select_option + 1) % len(options)

                    elif event.key == pygame.K_RETURN:
                        option_selected = options[select_option]
                        print(option_selected)

                        if (option_selected.lower() == 'play'):
                            print('play option')

                            self.init_game_mtd()
                            pygame.quit()

                        elif (option_selected.lower() == 'score'):
                            print('score option')

                            self.init_score_mtd()
                            pygame.quit()

                        elif (option_selected.lower() == 'about'):
                            print('about option')

                            self.init_about_mtd()
                            pygame.quit()
