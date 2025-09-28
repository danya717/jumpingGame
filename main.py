import arcade
import random

from cons import *
from log import MainLog
from log import MapLogs
from characters import Monkey
from clouds import Cloud
from barriers import JumpBarrier
from barriers import SmallJumpBarrier

MONKEY_SPEED = 5
MONKEY_JUMP = 5
MONKEY_Y_LIMIT = 310


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.log = MainLog()
        # self.mapLogs = MapLogs()
        self.monkey = Monkey()
        self.jump_barrier = JumpBarrier()
        self.small_jump_barrier = SmallJumpBarrier()
        self.cloud = Cloud()
        self.score = 0
        self.game = True
        self.lose = False
        self.start_again = False
        self.monkey_jump = True
        self.log_list = arcade.SpriteList()

    def setup(self):
        if self.game:
            for i in range(5):
                # self.mapLogs.center_x = 0
                # self.mapLogs.center_x = random.randint(0, SCREEN_WIDTH)
                map_logs = MapLogs()
                map_logs.center_x = 0
                map_logs.center_x = random.randint(0, SCREEN_WIDTH)
                map_logs.center_y = i * DISTANCE + SCREEN_HEIGHT
                self.log_list.append(map_logs)

    def on_draw(self):
        if self.game:
            self.clear()
            arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, (100, 0, 200))
            self.cloud.draw()
            self.log.draw()
            # self.mapLogs.draw()
            self.log_list.draw()
            self.monkey.draw()
            self.jump_barrier.draw()
            self.small_jump_barrier.draw()


            arcade.draw_text(f'SCORE: {self.score}', SCREEN_WIDTH - 445, SCREEN_HEIGHT - 20, (255, 255, 255), 15)
        if self.lose:
            self.game = False
            arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                         (0, 0, 0))
            arcade.draw_text("GAME OVER", SCREEN_WIDTH - 310, SCREEN_HEIGHT - 100, (255, 255, 255), 20)
            arcade.draw_text(f"SCORE:{self.score}", SCREEN_WIDTH - 290, SCREEN_HEIGHT - 180, (255, 255, 255), 20)
            arcade.draw_text("PRESS 'SPACE' TO START", SCREEN_WIDTH - 390, SCREEN_HEIGHT - 260, (255, 255, 255), 20)


    def update(self, delta_time: float):
        if self.game:
            self.monkey.update()
            # self.mapLogs.update()
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
            # if monkey goes under the screen it's lose
            if self.monkey.center_y < 0:
                self.lose = True
            #monkey can be on the main log
            if arcade.check_for_collision(self.monkey, self.log):
                self.monkey_jump = True
                self.monkey.change_y = 0
                self.monkey.center_y = self.log.center_y + 118
            # if monkey get hit with the map log
            # if arcade.check_for_collision(self.monkey, self.mapLogs):
            #     self.lose = True
            #monkey can be on the map log
            if arcade.check_for_collision(self.monkey, self.small_jump_barrier):
                self.monkey.center_y = self.small_jump_barrier.center_y + 28
                self.monkey_jump = True
                self.jump_barrier.center_y = 460
                self.score = 10
            # configuration the jump barrier
            if self.monkey.center_y < self.small_jump_barrier.center_y:
                self.jump_barrier.center_y = 350

    def on_key_press(self, key: int, modifiers: int):
        if self.game:
            if key == arcade.key.A:
                self.monkey.change_x = -MONKEY_SPEED
            if key == arcade.key.D:
                self.monkey.change_x = MONKEY_SPEED
        if not self.game:
            if self.lose:
                if key == arcade.key.SPACE:
                    print("true")
                    self.game = True


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