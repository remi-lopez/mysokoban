import pygame as pg
import os

root = os.path.dirname(os.path.abspath(__file__))


class Player:
    def __init__(self):
        self.image = pg.image.load(root + '/themes/rick_and_morty/player.jpg').convert()
        self.left = pg.image.load(root + '/themes/rick_and_morty/player_left.jpg').convert()
        self.right = pg.image.load(root + '/themes/rick_and_morty/player_right.jpg').convert()
        self.up = pg.image.load(root + '/themes/rick_and_morty/player_up.jpg').convert()


class Wall:
    def __init__(self):
        self.image = pg.image.load(root + '/themes/rick_and_morty/wall_old.png').convert()


class Box:
    def __init__(self):
        self.image = pg.image.load(root + '/themes/rick_and_morty/box.jpg').convert()


class BoxOnTarget:
    def __init__(self):
        self.image = pg.image.load(root + '/themes/rick_and_morty/box_on_target.jpg').convert()


class Target:
    def __init__(self):
        self.image = pg.image.load(root + '/themes/rick_and_morty/target.jpg').convert()


class Space:
    def __init__(self):
        self.image = pg.image.load(root + '/themes/rick_and_morty/space.jpg').convert()
