import arcade

class Monkey(arcade.Sprite):
    def __init__(self):
        super().__init__('monkey 2d.png', 0.06)
        self.center_x = 218
        self.center_y = 147