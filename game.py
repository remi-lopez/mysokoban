import sys
import pygame
from pygame.locals import *
from pygame import mixer
from models import *
from menu import *
from sound import *


root = os.path.dirname(os.path.abspath(__file__))

SIZE = 36
PLAYER = '@'
TARGET = '.'
SPACE = ' '
BOX = '$'
BINGO = '*'
WALL = '#'


class Game:
    def __init__(self):
        self.filename = File()
        self.board = Board()
        self.objective = Objective()
        self.screen = Screen()
        self.key = 'DOWN'

    def start(self):
        """ Launch new game """
        self.filename.get_saved_level()
        self.board.lines = self.board.initialize(self.filename.get_level())
        self.objective.targets = self.objective.initialize(self.board.lines)
        self.screen.size = self.screen.get_screen_size(self.board.lines)

    def do_move(self, row, col, i, j):
        self.board.lines[row + i][col + j] = PLAYER
        if self.objective.is_target(row, col):
            self.board.lines[row][col] = TARGET
        else:
            self.board.lines[row][col] = SPACE

    def check_win(self):
        """ Check if all the box are on the targets : go to next level """
        all_on_target = True
        for target in self.objective.targets:
            if self.board.lines[target[0]][target[1]] != BINGO:
                all_on_target = False
                break

        if all_on_target:
            reset_song = mixer.Sound('songs/win.wav')
            reset_song.play()
            reset_song.set_volume(1)
            self.filename.number = self.filename.number + 1
            self.filename.save_level()
            self.reset()

    def draw(self, screen):
        """ Draw board using images and check if all the box are on the targets"""
        player = Player().set_player(self.key)

        images = {
            WALL: Wall().image,
            BOX: Box().image,
            BINGO: BoxOnTarget().image,
            SPACE: Space().image,
            TARGET: Target().image,
            PLAYER: player,
        }

        self.board.draw(screen, images)
        pygame.display.update()

        self.check_win()

    def reset(self):
        """ Reset current level - restart board, targets and screen """
        self.board.lines.clear()
        self.objective.targets.clear()
        self.start()

    def move_player(self, i, j):
        row, col = self.board.player_position()

        m, n = i * 2, j * 2

        if self.board.lines[row + i][col + j] == SPACE:
            self.do_move(row, col, i, j)
        elif self.board.lines[row + i][col + j] == TARGET:
            self.do_move(row, col, i, j)
        elif self.board.lines[row + i][col + j] == BOX:
            if self.board.lines[row + m][col + n] == SPACE:
                self.board.lines[row + m][col + n] = BOX
                self.do_move(row, col, i, j)
            elif self.board.lines[row + m][col + n] == TARGET:
                Sound().set_sound('songs/targeted.wav', 0.6)
                self.board.lines[row + m][col + n] = BINGO
                self.do_move(row, col, i, j)
        elif self.board.lines[row + i][col + j] == BINGO:
            if self.board.lines[row + m][col + n] == SPACE:
                self.board.lines[row + m][col + n] = BOX
                self.do_move(row, col, i, j)
            elif self.board.lines[row + m][col + n] == TARGET:
                self.board.lines[row + m][col + n] = BINGO
                self.do_move(row, col, i, j)
        else:
            Sound().set_sound('songs/walk.wav', 0.1)
            pass

    def play(self, screen):
        """ Main loop : handle Quit, move and menu """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
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
                    Sound().set_sound('songs/wubba.wav', 0.6)
                    self.reset()
                elif event.key == pygame.K_m:
                    mixer.music.pause()
                elif event.key == pygame.K_p:
                    mixer.music.unpause()

                # MENU
                elif event.key == pygame.K_SPACE:
                    menu = Menu(self.screen.size)
                    show_menu = menu.toggle_menu()

                    if show_menu:
                        action = menu.show()
                        if action == "replay":
                            Sound().set_sound('songs/wubba.wav', 0.6)
                            self.reset()
                        elif action == "mute":
                            mixer.music.pause()
                        elif action == "unmute":
                            mixer.music.unpause()
                        elif action == "quit":
                            pygame.quit()
                            sys.exit()

        self.draw(screen)
