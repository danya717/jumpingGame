import arcade

class Barrier(arcade.Sprite):
    def __init__(self, scale):
        super().__init__('jumpBarrier.png', scale)
        # self.alpha = True

class JumpBarrier(Barrier):
    def __init__(self):
        super().__init__(1.2)
        self.center_x = 225
        self.center_y = 350

class SmallBarrier(arcade.Sprite):
    def __init__(self, scale):
        super().__init__('small_barrier.png', scale)
        # self.alpha = True

class SmallJumpBarrier(SmallBarrier):
    def __init__(self):
        super().__init__(1.4)
        self.center_x = 100
        self.center_y = 257