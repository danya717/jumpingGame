import arcade

class Log(arcade.Sprite):
    def __init__(self):
        super().__init__("log.png", 0.9)
        self.center_x = 215
        self.center_y = 30