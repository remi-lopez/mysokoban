import pygame
from pygame.locals import *
from pygame import mixer


class Sound:
    @staticmethod
    def intro():
        mixer.music.load('songs/intro.wav')
        mixer.music.play()
        mixer.music.queue('songs/theme.wav')
        mixer.music.play()
        mixer.music.set_volume(0.3)

    @staticmethod
    def set_sound(path, volume):
        reset_song = mixer.Sound(path)
        reset_song.play()
        reset_song.set_volume(volume)
