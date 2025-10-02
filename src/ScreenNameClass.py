import pygame
import sys
import os


class ScreenName():

    # Constants for colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)

    # Constants
    WIDTH = 800
    HEIGHT = 600

    # Constructor for this class
    def __init__(self, score, finish_mtd):
        pygame.init()

        # Getting the surface
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Introduce your name')

        # Preparing varibles for title and subtitle
        self.font_title = pygame.font.Font(None, 30)
        self.font_subtitle = pygame.font.Font(None, 36)
        self.font_input = pygame.font.Font(None, 36)

        # Preparing variables for inputs
        self.text_input = ''
        self.input_active = False

        # Loading backgroung image
        self.background = self.load_img('background1.jpg')
        self.score = score

        # Creating the title
        text_title = 'Congratulations! You have exceeded the maximum socore. Enter your name'
        render_title = self.font_title.render(text_title, True, self.WHITE)
        rect_title = render_title.get_rect(center=(self.WIDTH/2, 50))

        # Creating the subtitle
        text_subtitle = 'Space Invader Proyect Hybridge'
        render_subtitle = self.font_title.render(
            text_subtitle, True, self.WHITE)
        rect_subtitle = render_subtitle.get_rect(center=(self.WIDTH/2, 100))

        # Creating the object for the input box
        input_box = pygame.Rect(200, 200, 400, 50)
        accept_button = pygame.Rect(300, 300, 200, 50)

        # Runing the program
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Detecting if the click the back button
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # Detecting if we click the input box
                    if input_box.collidepoint(event.pos):
                        self.input_active = not self.input_active
                    else:
                        self.input_active = False

                # Detecting when we are writing
                if event.type == pygame.KEYDOWN:

                    # If is active
                    if self.input_active:

                        # Press enter
                        if event.key == pygame.K_RETURN:
                            print(self.text_input)
                            self.text_input = ''

                        # Press delete
                        elif event.key == pygame.K_BACKSPACE:
                            self.text_input = self.text_input[:-1]

                        # Press any key
                        else:
                            self.text_input += event.unicode

                # Pressing accept button
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # Detecting if you pressed accepte button
                    if accept_button.collidepoint(event.pos):
                        print('Text introduced:', self.text_input)
                        self.write_in_file(
                            'scores.txt', self.text_input + ',' + str(self.score))
                        finish_mtd()
                        pygame.quit()

            self.window.blit(self.background, (0, 0))

            # Drawing the title
            pygame.draw.rect(self.window, self.BLACK, rect_title)
            self.window.blit(render_title, rect_title)

            # Drawing subtitle
            pygame.draw.rect(self.window, self.BLACK, rect_subtitle)
            self.window.blit(render_subtitle, rect_subtitle)

            # If input is not active will be gray out
            color_input = self.GRAY if not self.input_active else self.WHITE

            # Drawing the text in the input box
            pygame.draw.rect(self.window, color_input, input_box, 2)
            surface_text = self.font_input.render(
                self.text_input, True, self.WHITE)
            self.window.blit(surface_text, (input_box.x + 5, input_box.y + 5))

            # Drawing the accept button
            pygame.draw.rect(self.window, self.GRAY, accept_button)
            button_text = self.font_input.render('Accept', True, self.BLACK)
            button_text_rect = button_text.get_rect(
                center=accept_button.center)
            self.window.blit(button_text, button_text_rect)

            pygame.display.flip()

    # Loading image
    def load_img(self, filename):

        path = 'src/img/' + filename
        return pygame.transform.scale(pygame.image.load(path).convert(), (self.WIDTH, self.HEIGHT))

    # Writing in the file
    def write_in_file(self, filename, content):

        current_dir = os.getcwd()
        path = os.path.join(current_dir, filename)

        # Detecting if the file is already created
        try:
            if not os.path.exists(path):
                with open(path, 'w') as file:
                    file.write(content + '\n')
                    print(f'file {path} created and content wrote')
            else:
                print(f'File {path} already created')
                with open(path, 'a') as file:
                    file.write(content + '\n')

        except PermissionError:
            print('You don\'t have access to this file:' +
                  f'\'{os.path.dirname(path)}\'')
        except Exception as e:
            print(f'Error at creating or write in file: {e}')

    def finish():
        print("finished")
