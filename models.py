import pygame
import os
from os.path import exists


root = os.path.dirname(os.path.abspath(__file__))

SIZE = 36
PLAYER = '@'
TARGET = '.'
SPACE = ' '
BOX = '$'
BINGO = '*'
WALL = '#'


class File:
    def __init__(self):
        """ On construct : return level(str) + number(int) """
        self.name = 'level'
        self.number = 1

    def get_level(self):
        """ Return current level (str) """
        return self.name + str(self.number)

    def save_level(self):
        """ Save current level to backup.txt """
        f = open('backup.txt', 'w+')
        f.write(self.get_level())
        f.close()

    def get_saved_level(self):
        """ Get current level into backup.txt """
        file_exists = exists('backup.txt')

        if file_exists:
            with open('backup.txt') as f:
                level = f.read()
                self.number = int(level[5:])


class Screen:
    def __init__(self):
        self.size = None

    def get_screen_size(self, board):
        """ return screen size using Board() length """
        j = 0
        for i in range(len(board)):
            j = len(board[i]) if len(board[i]) > j else j

        self.size = j * SIZE, len(board) * SIZE
        return self.size


class Board:
    def __init__(self):
        self.lines = []

    def initialize(self, filename: str):
        """ return current boardgame by reading file """
        with open(root + '/levels/%s' % filename, 'r') as f:
            for line in f.read().splitlines():
                self.lines.append(list(line))
            return self.lines

    def player_position(self):
        """ return player position on boardgame """
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                if self.lines[i][j] == PLAYER:
                    return i, j

    def draw(self, screen, images):
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                screen.blit(images[self.lines[i][j]], (j * SIZE, i * SIZE))


class Objective:
    def __init__(self):
        self.targets = []

    def initialize(self, board):
        """ return targets present on current boardgame """
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == TARGET:
                    self.targets.append([i, j])
        return self.targets

    def is_target(self, row, col):
        """ return boolean if is target """
        for target in self.targets:
            if target[0] == row and target[1] == col:
                return True
        return False


class Player:
    def __init__(self):
        self.image = pygame.image.load(root + '/themes/rick_and_morty/player.jpg').convert()
        self.left = pygame.image.load(root + '/themes/rick_and_morty/player_left.jpg').convert()
        self.right = pygame.image.load(root + '/themes/rick_and_morty/player_right.jpg').convert()
        self.up = pygame.image.load(root + '/themes/rick_and_morty/player_up.jpg').convert()

    @staticmethod
    def set_player(key):
        """ return player image depends on event.key """
        new_player = Player()

        if key == 'UP':
            return new_player.up
        elif key == 'LEFT':
            return new_player.left
        elif key == 'RIGHT':
            return new_player.right
        else:
            return new_player.image


class Wall:
    def __init__(self):
        self.image = pygame.image.load(root + '/themes/rick_and_morty/wall_old.png').convert()


class Box:
    def __init__(self):
        self.image = pygame.image.load(root + '/themes/rick_and_morty/box.jpg').convert()


class BoxOnTarget:
    def __init__(self):
        self.image = pygame.image.load(root + '/themes/rick_and_morty/box_on_target.jpg').convert()


class Target:
    def __init__(self):
        self.image = pygame.image.load(root + '/themes/rick_and_morty/target.jpg').convert()


class Space:
    def __init__(self):
        self.image = pygame.image.load(root + '/themes/rick_and_morty/space.jpg').convert()
