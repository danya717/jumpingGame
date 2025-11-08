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

class MovingPlats(Platform):
    def __init__(self):
        super().__init__(0.6)
        self.change_x = 2
        self.can_move_left = True
        self.can_move_right = False

    def update(self):
        if self.can_move_left:
            self.center_x -= self.change_x
        if self.center_x < 0:
            self.can_move_left = False
            self.can_move_right = True
        if self.can_move_right:
            self.center_x += self.change_x
        if self.center_x > SCREEN_WIDTH:
            self.can_move_right = False
            self.can_move_left = True

