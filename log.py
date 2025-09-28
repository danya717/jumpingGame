import arcade
import random

from arcade.examples.dual_stick_shooter import SCREEN_HEIGHT

import cons

class Log(arcade.Sprite):
    def __init__(self, scale):
        super().__init__("log.png", scale)

class MainLog(Log):
    def __init__(self):
        super().__init__(1)
        self.center_x = 215
        self.center_y = 30

class MapLogs(Log):
    def __init__(self):
        super().__init__(0.6)
        # self.center_x = 100
        # self.center_y = 200