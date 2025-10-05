import pygame
import sys
import os
import webbrowser

# Class for the menu about, in the main menu

class About():

    # Constants for colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (200, 200, 200)
    RED = (255, 0, 0)

    # Constants
    WIDTH = 800
    HEIGHT = 600

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption('About')

    # Constructor
    
    def __init__(self, back_mtd):
        self.back_mtd = back_mtd

    # looking for the image to load it
    def load_img(self, filename):
        path = os.path.join('./img', filename)

        return pygame.image.load(path).convert_alpha()

    # show text
    def show_text(self, text, font, color, surface, x, y):

        text_obj = font.render(text, True, color)
        rect_text = text_obj.get_rect()
        rect_text.topleft = (x, y)
        surface.blit(text_obj, rect_text)

     # Drawing the button to go back
    def draw_button(self, text, font, color, surface, x, y, width, height):

        # Transform the button on a rect object
        pygame.draw.rect(surface, color, (x, y, width, height))

        # Getting the text size
        text_width, text_height = font.size(text)

        # Drawing the text in the rect object without getting out of the object
        text_x = x + (width - text_width) // 2
        text_y = y + (height - text_height) // 2

        self.show_text(text, font, self.BLACK, surface, text_x, text_y)

    # Showing the content
    def show_content(self, content, font_content, y_offset):

        horizontal_space_available = self.WIDTH - 100

        # Spliting the text
        for line in content.split('\n'):
            words = line.split()
            line_text = ''

            # Append ecah word whith a space
            for word in words:
                line_text_temp = line_text + word + ' '
                text_width_temp = font_content.size(line_text_temp)[0]

                # Checking if we have space available in the line
                if text_width_temp < horizontal_space_available:
                    line_text = line_text_temp

                else:

                    # Drawing the text
                    self.show_text(line_text.strip(), font_content, self.WHITE, self.WIN, (
                        self.WIDTH - font_content.size(line_text.strip())[0]) // 2, y_offset)

                    # Taking the height to separate correctly the text
                    y_offset += font_content.size(line_text.strip())[1]
                    line_text = word + ' '

            # When you finished the full text
            self.show_text(line_text.strip(), font_content, self.WHITE, self.WIN, (
                self.WIDTH - font_content.size(line_text.strip())[0]) // 2, y_offset)
            y_offset += font_content.size(line_text.strip())[1]

    # Method to show the menu
     
    def show_menu(self):

        self.WIN.fill(self.BLACK)

        # Loading the background image
        background = self.load_img('background1.jpg')

        background = pygame.transform.scale(
            background, (self.WIDTH, self.HEIGHT))

        self.WIN.blit(background, (0, 0))

        # Drawing the title
        text_title = 'About'
        font_title = pygame.font.Font(None, 48)
        title_width = font_title.size(text_title)[0]

        title_x = (self.WIDTH - title_width) // 2

        self.show_text(text_title, font_title,
                       self.WHITE, self.WIN, title_x, 50)

        # Drawing the subtitle
        subtext_title = 'Space Inveders Project'
        sub_font_title = pygame.font.Font(None, 36)
        subtitle_width = sub_font_title.size(subtext_title)[0]

        subtitle_x = (self.WIDTH - subtitle_width) // 2

        self.show_text(subtext_title, sub_font_title,
                       self.WHITE, self.WIN, subtitle_x, 120)

        # Drawing the content
        content = 'Hi! I\'m Bruno, and this is the final project for the \"Object-Oriented Programming\" course.\n A collaborative video game created as final project , with some added features.\nThese include crash damage, sounds when crashing, and some gifts or treasures that could help you on your adventure.\nThanks to all my teachers for sharing their knowledge.\nEnjoy!'
        font_content = pygame.font.Font(None, 30)
        y_offset = max(200, sub_font_title.size(subtext_title)[1] + 120)

        self.show_content(content, font_content, y_offset)

        ################# Add a link ###############
        link_title = 'My LinkedIn link'
        link_font = pygame.font.Font(None, 36)
        link_width = link_font.size(link_title)[0]

        link_x = (self.WIDTH - link_width) // 2

        self.show_text(link_title, link_font,
                       self.RED, self.WIN, link_x, 500)

        pygame.draw.rect(self.WIN, self.GREY, (20, 20, 50, 50))

        # Drawing the back button
        self.draw_button('<', pygame.font.Font(None, 36),
                         self.GREY, self.WIN, 20, 20, 50, 50)
        pygame.display.update()

    # Run the program
    def run(self):
        self.show_menu()

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
                            self.back_mtd()

                        # Using webbrowser to open the link
                        elif 200 <= x <= self.WIDTH-200 and 300 <= y < 520:
                            webbrowser.open(
                                'https://www.linkedin.com/in/bruno-delgado-15301a388')
