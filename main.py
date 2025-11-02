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
        self.can_score = True
        self.main_platform_draw = True
        self.times_can_jump_on_plat = 0
        # self.jump_barrier_can_go_y = 0
        self.platform_list = arcade.SpriteList()
        self.plat_list = arcade.SpriteList()
        self.barrier_list = arcade.SpriteList()
        self.plat_barriers = SmallJumpBarrier()
        # self.engine = PhysicsEnginePlatformer(self.monkey, self.platform_list, GRAVITY)
        self.time = time.time()
        self.last_platform = None

        # self.uses = 0
        # self.max_uses = 5

    def setup(self):
        if self.game:
            self.jump_barrier.center_y = START_JUMP_BARRIER_DISTANCE
            self.platform_list = arcade.SpriteList()
            self.barrier_list = arcade.SpriteList()
            for i in range(5):
                plats = MapPlats()
                plats.center_y = i * DISTANCE + PLATS_DISTANCE
                plats.center_x = random.randint(50, SCREEN_WIDTH - MAX_WIDTH_DISTANCE)
                plats.uses = 0
                plats.max_uses = 5
                plats.scored = False
                self.platform_list.append(plats)
            for i in range(3):
                barriers = SmallJumpBarrier()
                barriers.center_y = i * DISTANCE + MAP_BARRIERS_CORRECT_PLACE
                barriers.center_x = 100
                self.barrier_list.append(barriers)
            for i in range(1):
                plat = MapPlats()
                plat.center_y = i * DISTANCE + 100
                plat.center_x = 50
                self.plat_list.append(plat)
            for i in range(1):
                plat = MapPlats()
                plat.center_y = i * DISTANCE + 200
                plat.center_x = 300
                self.plat_list.append(plat)


    def on_draw(self):
        if self.game:
            self.clear()
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
            self.cloud.draw()
            if self.main_platform_draw:
                self.platform.draw()
            self.platform_list.draw()
            self.plat_list.draw()
            # self.barrier_list.draw()
            # self.barrier_list.draw()
            self.monkey.draw()
            self.jump_barrier.draw()
            # self.plat_barriers.draw()

            arcade.draw_text(f'SCORE: {self.score}', SCREEN_WIDTH - 395, SCREEN_HEIGHT - 20, (255, 255, 255), 15)
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
            if self.main_platform_draw:
                if arcade.check_for_collision(self.monkey, self.platform):
                    self.jump_barrier.center_y = START_JUMP_BARRIER_DISTANCE
                    self.monkey_jump = True
                    self.monkey.change_y = 0
                    self.monkey.center_y = self.platform.center_y + MAIN_PLATFORM_DISTANCE

            if arcade.check_for_collision(self.monkey, self.plat_list[0]):
                self.jump_barrier.center_y = AFTER_JUMPING_ON_THE_FIRST_PLAT_DISTANCE
                self.monkey.center_y = self.plat_list[0].center_y + DISTANCE_TO_TOP_PLAT
                self.monkey_jump = True

            if arcade.check_for_collision(self.monkey, self.plat_list[1]):
                self.jump_barrier.center_y = AFTER_JUMPING_ON_THE_FIRST_PLAT_DISTANCE + 80
                self.monkey.center_y = self.plat_list[1].center_y + DISTANCE_TO_TOP_PLAT
                self.monkey_jump = True


            for plat in self.platform_list:
                if arcade.check_for_collision(self.monkey, plat):
                    self.monkey.center_y = plat.center_y + DISTANCE_TO_TOP_PLAT
                    self.monkey_jump = True
                    if self.last_platform is not plat:
                        if not hasattr(plat, "uses"):
                            plat.uses = 0
                            plat.max_uses = 5
                        if not hasattr(plat, "scored"):
                            plat.scored = False
                        plat.uses += 1

                        self.times_can_jump_on_plat += 1
                        if plat.uses >= plat.max_uses:
                            self.platform_list.remove(plat)
                            self.last_platform = None
                            break
                        else:
                            self.last_platform = plat
                    else:
                        self.last_platform = plat
                    if not plat.scored:
                        plat.scored = True
                        dy = DISTANCE
                        self.main_platform_draw = False
                        # self.jump_barrier.center_y = MONKEY_Y_LIMIT
                        for p in self.platform_list:
                            p.center_y -= dy
                            if p.center_y < 0:
                                p.center_y = SCREEN_HEIGHT + 50
                        for p in self.plat_list:
                            p.center_y -= dy

                        # for b in self.barrier_list:
                        #     b.center_y -= dy
                        #     if b.center_y < 0:
                        #         b.center_y = SCREEN_HEIGHT + 200

                        break
                    else:
                        self.last_platform = None

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
                    self.main_platform_draw = True
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