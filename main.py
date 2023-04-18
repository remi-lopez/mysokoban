import pygame
from pygame.locals import *
from pygame import mixer
from game import *
from sound import *


def main():
    game = Game()
    game.start()

    pygame.init()
    pygame.display.init()
    pygame.display.set_caption('My Sokoban')

    screen = pygame.display.set_mode(game.screen.size)
    bg_img = pygame.transform.scale(
        pygame.image.load('themes/space.png'),
        game.screen.size
    )

    mixer.init()
    Sound().intro()

    while True:
        screen.blit(bg_img, (0, 0))
        game.play(screen)


if __name__ == '__main__':
    main()
