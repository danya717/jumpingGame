import arcade

class Monkey(arcade.Sprite):
    def __init__(self):
        super().__init__('monkey 2d.png', scale=0.06)
        self.center_x = 218
        self.center_y = 147
        self.side = True
        self.left_texture = arcade.load_texture('monkey 2d.png', flipped_horizontally=True)
        self.right_texture = arcade.load_texture('monkey 2d.png')

    def set_side(self):
        if self.side:
            self.texture = self.right_texture
        else:
            self.texture = self.left_texture