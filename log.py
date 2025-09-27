import arcade
import random

class Log(arcade.Sprite):
    def __init__(self):
        super().__init__("log.png")

class MainLog(Log):
    def __init__(self):
        super().__init__()
        self.center_x = 215
        self.center_y = 30

class MapLogs(Log):
    def __init__(self):
        super().__init__()
        self.center_x = random.randint(100, 350)
        self.center_y = random.randint(100, 200)