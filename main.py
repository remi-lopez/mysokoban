import sys
import pygame
import os

from models import *

CELL_SIZE = 36

PLAYER = '@'
TARGET = '.'
SPACE = ' '
BOX = '$'
BINGO = '*'
WALL = '#'

root = os.path.dirname(os.path.abspath(__file__))


class File:
    def __init__(self):
        self.name = 'level'
        self.number = 1

    def get_level(self):
        return self.name + str(self.number)

    def next_level(self):
        self.number = self.number + 1
        return self.name + str(self.number)


class Screen:
    @staticmethod
    def get_screen_size(board):
        j = 0
        for i in range(len(board)):
            j = len(board[i]) if len(board[i]) > j else j

        return j * CELL_SIZE, len(board) * CELL_SIZE


class Board:
    def __init__(self):
        self.board = []

    def initialize(self, filename: str):
        with open(root + '/levels/%s' % filename, 'r') as f:
            for line in f.read().splitlines():
                self.board.append(list(line))
            return self.board

    def get_length(self):
        return len(self.board)


class Targets:
    def __init__(self):
        self.targets = []

    def initialize(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == TARGET:
                    self.targets.append([i, j])
        return self.targets

    def is_target(self, row, col):
        for target in self.targets:
            if target[0] == row and target[1] == col:
                return True
        return False


class Game:
    def __init__(self):
        self.filename = File()
        self.board = Board().initialize(self.filename.get_level())
        self.targets = Targets().initialize(self.board)
        self.screen = Screen().get_screen_size(self.board)
        self.key = 'DOWN'

    def is_target(self, row, col):
        for target in self.targets:
            if target[0] == row and target[1] == col:
                return True
        return False

    def player_position(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == PLAYER:
                    return i, j

    def move_player(self, i, j):
        row, col = self.player_position()

        m, n = i * 2, j * 2

        if self.board[row + i][col + j] == SPACE:
            self.do_move(row, col, i, j)
        elif self.board[row + i][col + j] == TARGET:
            self.do_move(row, col, i, j)
        elif self.board[row + i][col + j] == BOX:
            if self.board[row + m][col + n] == SPACE:
                self.board[row + m][col + n] = BOX
                self.do_move(row, col, i, j)
            elif self.board[row + m][col + n] == TARGET:
                self.board[row + m][col + n] = BINGO
                self.do_move(row, col, i, j)
        elif self.board[row + i][col + j] == BINGO:
            if self.board[row + m][col + n] == SPACE:
                self.board[row + m][col + n] = BOX
                self.do_move(row, col, i, j)
            elif self.board[row + m][col + n] == TARGET:
                self.board[row + m][col + n] = BINGO
                self.do_move(row, col, i, j)
        else:
            pass

    def do_move(self, row, col, i, j):
        self.board[row + i][col + j] = PLAYER
        if self.is_target(row, col):
            self.board[row][col] = TARGET
        else:
            self.board[row][col] = SPACE

    def check_win(self):
        all_on_target = True
        for target in self.targets:
            if self.board[target[0]][target[1]] != BINGO:
                all_on_target = False
                break

        if all_on_target:
            self.filename.number = self.filename.number + 1
            self.reset(self.filename.get_level())

    def set_player(self):
        new_player = Player()

        if self.key == 'DOWN':
            return new_player.image
        elif self.key == 'UP':
            return new_player.up
        elif self.key == 'LEFT':
            return new_player.left
        elif self.key == 'RIGHT':
            return new_player.right

    def draw(self, screen):
        player = self.set_player()

        images = {
            WALL: Wall().image,
            BOX: Box().image,
            BINGO: BoxOnTarget().image,
            SPACE: Space().image,
            TARGET: Target().image,
            PLAYER: player,
        }

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                screen.blit(
                    images[self.board[i][j]],
                    (j * CELL_SIZE, i * CELL_SIZE)
                )

        pygame.display.update()
        self.check_win()

    def play(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.move_player(-1, 0)
                    self.key = 'UP'
                elif event.key == pygame.K_RIGHT:
                    self.move_player(0, 1)
                    self.key = 'RIGHT'
                elif event.key == pygame.K_DOWN:
                    self.move_player(1, 0)
                    self.key = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    self.move_player(0, -1)
                    self.key = 'LEFT'
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    self.reset(self.filename.get_level())
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.draw(screen)

    def reset(self, filename):
        self.board.clear()
        self.targets.clear()
        self.board = Board().initialize(filename)
        self.targets = Targets().initialize(self.board)
        self.screen = Screen().get_screen_size(self.board)


def main():
    game = Game()

    pygame.init()
    pygame.display.init()
    pygame.display.set_caption('My Sokoban')

    screen = pygame.display.set_mode(game.screen)
    screen.fill((0, 0, 0))

    while True:
        game.play(screen)


if __name__ == '__main__':
    main()
