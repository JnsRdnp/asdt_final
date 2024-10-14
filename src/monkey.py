import pygame
from toneplayer import Note
import time
import random
from pygame.mixer import pre_init

class Monkey():
    pygame.font.init()

    def __init__(self, colors, x, y, screen):
        pre_init(44100, -16, 1, 1024)

        self.color = colors["magenta"]
        self.x = x
        self.y = y
        self.screen = screen
        self.size = 7

        self.update()
        self.play_random_sound()


    def play_random_sound(self):
        random_hz = random.randint(400,2000)
        Beep = Note(random_hz).play(-1)
        time.sleep(1)
        Beep.stop()


    def living_sounds(self):
        lava_sound = pygame.mixer.Sound('./assets/lava.wav')
        lava_sound.play()
        lava_sound.fadeout(3000)


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape_rect, border_radius=5)


    def update(self):
        self.shape_rect = pygame.Rect(self.x,self.y,self.size,self.size)


        

