import arcade
from cons import *

class Bird(arcade.Sprite):
    def __init__(self):
        super().__init__('images/bird-Photoroom.png', 0.03)
        self.center_x = 100
        self.center_y = 100
        self.change_x = 1
        self.can_move_right = False
        self.can_move_left = True
        self.side = True
        self.left_texture = arcade.load_texture('images/bird-Photoroom.png', flipped_horizontally=True)
        self.right_texture = arcade.load_texture('images/bird-Photoroom.png')



    def set_side(self):
        if self.side:
            self.texture = self.left_texture
        else:
            self.texture = self.right_texture


    def update(self):
        if self.can_move_left:
            self.set_side()
            self.side = True
            self.center_x -= self.change_x
        if self.center_x < 0:
            self.can_move_left = False
            self.can_move_right = True
        if self.can_move_right:
            self.set_side()
            self.side = False
            self.center_x += self.change_x
        if self.center_x > SCREEN_WIDTH:
            self.can_move_right = False
            self.can_move_left = True


