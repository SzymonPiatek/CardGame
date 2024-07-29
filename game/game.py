import pygame as pg
import sys
from settings import *


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(settings["tick"])
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def update(self):
      pass

    def draw(self):
        self.screen.fill((settings["color"]["background"]))

        pg.display.flip()
