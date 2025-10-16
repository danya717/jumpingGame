import arcade
import random
import time

from cons import *
from platforms import MainPlat
from platforms import MapPlats
from characters import Monkey
from clouds import Cloud
from barriers import JumpBarrier
from barriers import SmallJumpBarrier

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("images/mainBg.png")
        self.platform = MainPlat()
        self.monkey = Monkey()
        self.jump_barrier = JumpBarrier()
        self.cloud = Cloud()
        self.score = 0
        self.game = True
        self.lose = False
        self.start_again = False
        self.monkey_jump = True
        # self.jump_barrier_can_go_y = 0
        self.platform_list = arcade.SpriteList()
        self.barrier_list = arcade.SpriteList()
        self.plat_barriers = SmallJumpBarrier()
        # self.engine = PhysicsEnginePlatformer(self.monkey, self.platform_list, GRAVITY)
        self.time = time.time()

    def setup(self):
        if self.game:
            self.platform_list = arcade.SpriteList()
            self.barrier_list = arcade.SpriteList()
            for i in range(5):
                plats = MapPlats()
                plats.center_y = i * DISTANCE + PLATS_DISTANCE
                plats.center_x = random.randint(50, SCREEN_WIDTH - MAX_WIDTH_DISTANCE)

                self.platform_list.append(plats)
                barriers = SmallJumpBarrier()
                barriers.center_y = plats.center_y + DISTANCE_BETWEEN_PLATS
                barriers.center_x = plats.center_x
                self.barrier_list.append(barriers)

    def on_draw(self):
        if self.game:
            self.clear()
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
            self.cloud.draw()
            self.platform.draw()
            self.platform_list.draw()
            # self.barrier_list.draw()
            self.monkey.draw()
            self.jump_barrier.draw()

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
            # self.engine.update()
            self.monkey.update()
            # monkey can jump up
            if self.monkey_jump:
                self.monkey.change_y = MONKEY_JUMP

            # jump can jump down
            if arcade.check_for_collision(self.monkey, self.jump_barrier):
                self.monkey_jump = False
                self.monkey.change_y = -MONKEY_JUMP

            #check if monkey can't go beyond the right screen
            if self.monkey.center_x > SCREEN_WIDTH - 20:
                self.monkey.change_x = 0

            # check if monkey can't go beyond the left screen
            if self.monkey.center_x < 0 + 20:
                self.monkey.change_x = 0

            # check if monkey goes under the screen it's lose
            if self.monkey.center_y < 0:
                self.lose = True

            #check that monkey can be on the main platform
            if arcade.check_for_collision(self.monkey, self.platform):
                self.monkey_jump = True
                self.monkey.change_y = 0
                self.monkey.center_y = self.platform.center_y + MAIN_PLATFORM_DISTANCE

            # configure the jump barrier
            if self.monkey.center_y < self.platform_list[0].center_y:
                self.jump_barrier.center_y = START_JUMP_BARRIER_DISTANCE

            # check collision that monkey can be on the platform 1
            # if arcade.check_for_collision(self.monkey, self.platform_list[0]):
            #     self.jump_barrier.center_y = 450
            #     self.monkey.center_y = self.platform_list[0].center_y + 80
            #     self.monkey_jump = True
            # check collision that monkey can be on the platform 2
            # if arcade.check_for_collision(self.monkey, self.platform_list[1]):
            #     self.jump_barrier.center_y = 600
            #     self.monkey.center_y = self.platform_list[1].center_y + 80
            #     self.monkey_jump = True

            for plat in self.platform_list:
                if arcade.check_for_collision(self.monkey, plat):
                    dy = DISTANCE
                    self.jump_barrier.center_y = MONKEY_Y_LIMIT
                    self.monkey.center_y = plat.center_y + DISTANCE_TO_TOP_PLAT
                    self.monkey_jump = True
                    for p in self.platform_list:
                        p.center_y -= dy
                        if p.center_y < 0:
                            p.center_y = SCREEN_HEIGHT

                    # for b in self.barrier_list:
                    #     b.center_y -= dy
                    #     if b.center_y < 0:
                    #         b.center_y = SCREEN_HEIGHT + 200

                    break

            # for barrier in self.barrier_list:
            #     if arcade.check_for_collision(self.monkey, barrier):
            #         self.lose = True

    def on_key_press(self, key: int, modifiers: int):
        if self.game:
            # monkey can go left
            if key == arcade.key.A:
                self.monkey.side = False
                self.monkey.set_side()
                self.monkey.change_x = -MONKEY_SPEED

            # monkey can go right
            if key == arcade.key.D:
                self.monkey.side = True
                self.monkey.set_side()
                self.monkey.change_x = MONKEY_SPEED

        # game can start again after lose
        if not self.game:
            if self.lose:
                if key == arcade.key.SPACE:
                    self.game = True
                    self.lose = False
                    self.score = 0
                    self.monkey.change_x = 0
                    self.monkey.change_y = 0
                    self.monkey.center_x = 218
                    self.monkey.center_y = 147
                    self.monkey_jump = True
                    self.setup()


    def on_key_release(self, key: int, modifiers: int):
        if self.game:
            if key == arcade.key.A:
                self.monkey.change_x = 0
            if key == arcade.key.D:
                self.monkey.change_x = 0

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x, y)


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
window.run()