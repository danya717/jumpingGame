import arcade
import random
import cons

class Platform(arcade.Sprite):
    def __init__(self, scale):
        super().__init__("log.png", scale)

class MainPlat(Platform):
    def __init__(self):
        super().__init__(1)
        self.center_x = 215
        self.center_y = 30

class MapPlats(Platform):
    def __init__(self):
        super().__init__(0.6)
        # self.center_x = random.randint(0, SCREEN_WIDTH)