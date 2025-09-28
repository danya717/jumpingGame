import arcade

class Cloud(arcade.Sprite):
    def __init__(self):
        super().__init__('cloud.png', 0.5)
        self.center_x = 250
        self.center_y = 300