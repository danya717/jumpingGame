import arcade
from cons import *
from log import Log
from characters import Monkey

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.log = Log()
        self.monkey = Monkey()

    def on_draw(self):
        self.clear()
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, (100, 0, 200))
        self.log.draw()
        self.monkey.draw()

    def update(self, delta_time: float):
        pass

    def on_key_press(self, key: int, modifiers: int):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x, y)


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.run()