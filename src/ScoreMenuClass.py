import pygame
import sys
import os

# Creating a class for scores

class Score():

    # Constants for colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (200, 200, 200)
    RED = (255, 0, 0)

    # Constants
    WIDTH = 800
    HEIGHT = 600

    # Creating a window
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Best score')

    # Constructor
    def __init__(self, back_mtd):
        self.back_mtd = back_mtd

    # Loading scores
    def load_scores(self, filename):

        scores = []

        # We read the data in the text file
        try:
            with open(filename, 'r') as file:

                for line in file:
                    name, score = line.strip().split(',')  # Slipt the data in the file
                    scores.append((name, int(score)))

        # Exception if the file is not found
        except FileNotFoundError:
            print(f'File did not found: {filename}')

        # Returning the scores in order and just the first 5
        return sorted(scores, key=lambda x: x[1], reverse=True)[:5]

    # Method to load the image with the scores
    def load_image(self, filename):

        path = os.path.join('src/img', filename)
        return pygame.image.load(path).convert_alpha()

    # Showing the text of the scores
    def show_text(self, text, font, color, surface, x, y):

        text_object = font.render(text, True, color)
        rec_text = text_object.get_rect()
        rec_text.center = (x, y)

        # Drawing the text
        surface.blit(text_object, rec_text)

    # Drawing the button for get back
    def draw_button(self, text, font, color, surface, x, y, width, height):

        # Transform the button on a rect object
        pygame.draw.rect(surface, color, (x, y, width, height))
        self.show_text(text, font, self.BLACK, surface,
                       x + width / 2, y + height / 2)

    # Show the scores
    def show_scores(self, scores):

        # Cleaning the windows
        self.window.fill(self.BLACK)

        # Loading and scaling the imgage
        background = self.load_image('background1.jpg')
        background = pygame.transform.scale(
            background, (self.WIDTH, self.HEIGHT))
        self.window.blit(background, (0, 0))

        # Creating the title
        self.show_text('Best Scores', pygame.font.Font(None, 48),
                       self.WHITE, self.window, self.WIDTH // 2, 50)

        # Creating the subtitles
        self.show_text('Space Invaders', pygame.font.Font(
            None, 36), self.WHITE, self.window, self.WIDTH//2, 120)

        # In case there is not scores yet
        if not scores:
            self.show_text('There is not scores yet', pygame.font.Font(
                None, 36), self.RED, self.window, self.WIDTH // 2, self.HEIGHT // 2)

        # Generating the offset for the scores
        else:
            y_offset = 250
            for i, (name, score) in enumerate(scores, 1):
                text_color = self.WHITE if i == 1 else self.RED
                font_size = 42 if i == 1 else 36
                self.show_text(f'{i}. {name}: {score}', pygame.font.Font(
                    None, font_size), text_color, self.window, self.WIDTH // 2, y_offset)
                y_offset += 60

        # Drawing the button
        self.draw_button('<', pygame.font.Font(None, 36),
                         self.GREY, self.window, 20, 20, 50, 50)
        pygame.display.update()

    # Runing the method
    def run(self):
        # Reading the file information
        scores = self.load_scores('scores.txt')
        self.show_scores(scores)

        # Runing the code
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Detecting if the click the back button
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        if 20 <= x <= 70 and 20 <= y <= 70:
                            print('Back action')
                            self.back_mtd()
