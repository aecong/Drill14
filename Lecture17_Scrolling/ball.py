from pico2d import *
import game_world
import game_framework
import random

from Lecture17_Scrolling import server


class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = random.randint(100, 1180)
        self.y = random.randint(100, 924)
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def set_background(self, bg):
        self.bg = bg

    def draw(self):
        sx, sy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.clip_draw(0, 0, 21, 21, sx, sy)

    def update(self):
        # self.window_left = clamp(0, int(server.boy.x) - self.cw // 2, self.w - self.cw - 1)
        # self.window_bottom = clamp(0, int(server.boy.y) - self.ch // 2, self.h - self.ch - 1)

        pass


    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                game_world.remove_object(self)
                pass