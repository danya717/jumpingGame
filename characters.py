import arcade
from cons import *


class Monkey(arcade.Sprite):
    def __init__(self):
        super().__init__('images/monkey 2d.png', scale=0.05)
        self.center_x = CHAR_CENTER_X
        self.center_y = CHAR_CENTER_Y
        self.side = True
        self.left_texture = arcade.load_texture('images/monkey 2d.png', flipped_horizontally=True)
        self.right_texture = arcade.load_texture('images/monkey 2d.png')

    def set_side(self):
        if self.side:
            self.texture = self.right_texture
        else:
            self.texture = self.left_texture