import arcade
from cons import *
from log import MainLog
from log import MapLogs
from characters import Monkey

MONKEY_SPEED = 2
MONKEY_JUMP = 4
MONKEY_Y_LIMIT = 310

class JumpBarrier(arcade.Sprite):
    def __init__(self):
        super().__init__('jumpBarrier.png', 1.2)
        self.center_x = 225
        self.center_y = 350
        # self.alpha = True

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.log = MainLog()
        self.mapLogs = MapLogs()
        self.monkey = Monkey()
        self.jump_barrier = JumpBarrier()
        self.score = 0
        self.game = True
        self.lose = False
        self.monkey_jump = True

    def on_draw(self):
        if self.game:
            self.clear()
            arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, (100, 0, 200))
            self.log.draw()
            self.mapLogs.draw()
            self.monkey.draw()
            self.jump_barrier.draw()
            if self.lose:
                arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                             (0, 0, 0))
                arcade.draw_text("You lost", SCREEN_WIDTH - 280, SCREEN_HEIGHT - 100, (255, 255, 255), 23)

    def update(self, delta_time: float):
        if self.game:
            self.monkey.update()
            if self.monkey_jump:
                self.monkey.change_y = MONKEY_JUMP
            #jump down for the monkey
            if arcade.check_for_collision(self.monkey, self.jump_barrier):
                self.monkey_jump = False
                self.monkey.change_y = -MONKEY_JUMP
            #monkey can't go beyond the right screen
            if self.monkey.center_x > SCREEN_WIDTH - 20:
                self.monkey.change_x = 0
            # monkey can't go beyond the left screen
            if self.monkey.center_x < 0 + 20:
                self.monkey.change_x = 0
            if self.monkey.center_y < 0:
                self.lose = True
            if arcade.check_for_collision(self.monkey, self.log):
                self.monkey_jump = True
                self.monkey.change_y = 0
                self.monkey.center_y = self.log.center_y + 118

    def on_key_press(self, key: int, modifiers: int):
        if self.game:
            if key == arcade.key.A:
                self.monkey.change_x = -MONKEY_SPEED
            if key == arcade.key.D:
                self.monkey.change_x = MONKEY_SPEED
            # if key == arcade.key.SPACE:



    def on_key_release(self, key: int, modifiers: int):
        if self.game:
            if key == arcade.key.A:
                self.monkey.change_x = 0
            if key == arcade.key.D:
                self.monkey.change_x = 0
            # if key == arcade.key.SPACE:
            #     self.monkey.change_y =

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x, y)


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.run()