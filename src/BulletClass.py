import pygame

# Creating the class for bullets


class Bullet():

    # Constructor
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

        # Create a mask to avoid false collisions
        self.mask = pygame.mask.from_surface(self.img)

    # Drawing the bullet
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, speed):
        self.y += speed

    # Detects collisions
    def collision(self, obj):

        # Compare the bullet mask with the obj mask to detect collitions
        offset = (
            int(self.x - obj.x - 30),
            int(self.y - obj.y - 20)
        )

        return self.mask.overlap(obj.mask, (offset))
