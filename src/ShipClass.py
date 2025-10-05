
# Creating a generic class for ships (After this, we got layer and enemys)

class Ship():
    def __init__(self, x, y, health=100): # We're going to set the coordinates and health
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.bullet_img = None
        self.bullet_cooldown_counter = 0
        self.bullets = []
        self.fired_bullets = []
        self.cool_down = 40

    # Drawing the ships
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    # Getting the width and height of the ship object --------------------------------

    # Getting the image width
    def get_width(self):
        return self.ship_img.get_width()

    # Getting the image height
    def get_height(self):
        return self.ship_img.get_height()
