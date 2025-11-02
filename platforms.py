import arcade
from cons import *

class Platform(arcade.Sprite):
    def __init__(self, scale):
        super().__init__("images/log.png", scale)

class MainPlat(Platform):
    def __init__(self):
        super().__init__(0.8)
        self.center_x = PLAT_CENTER_X
        self.center_y = PLAT_CENTER_Y

class MapPlats(Platform):
    def __init__(self):
        super().__init__(0.6)
        # self.center_x = random.randint(0, SCREEN_WIDTH)