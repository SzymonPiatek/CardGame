import pygame as pg
from game.game import Game
from settings import settings


def main():
    running = True
    playing = True

    pg.init()
    pg.mixer.init()

    screen = pg.display.set_mode((settings["screen"]["width"], settings["screen"]["height"]))
    clock = pg.time.Clock()
    game = Game(screen, clock)

    while running:
        while playing:
            game.run()


if __name__ == "__main__":
    main()