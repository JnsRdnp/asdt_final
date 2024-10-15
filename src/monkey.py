import pygame
from toneplayer import Note
import time
import random
# from pygame.mixer import pre_init
import threading


class Monkey():
    pygame.font.init()

    def __init__(self, colors, x, y, screen):
        pygame.mixer.init(frequency=44100, size=-16, channels=1)

        self.colors = colors
        self.x = x
        self.y = y
        self.screen = screen
        self.size = 7

        self.update()

        self.alive = True
        self.is_on_island = True # This boolean to handle dying of laughter
        self.is_civilized = False

        # threading.Thread(target=self.play_random_sound).start() # Commented out due to ear failure
        # threading.Thread(target=self.die_of_laughter).start()
        dying_handle = threading.Thread(target=self.die)
        dying_handle.start()

    def die(self): # Function to possibly die due to laughter or getting eaten by shark
        while self.alive:
            time.sleep(1)
            random_integer = random.randint(0,100)
            if random_integer == 99:
                self.alive=False


    def play_random_sound(self):
        while self.alive == True:
            random_hz = random.randint(400,2000)
            Beep = Note(random_hz)
            Beep.play(-1)
            time.sleep(1)
            Beep.stop()
            time.sleep(10)


    def living_sounds(self):
        lava_sound = pygame.mixer.Sound('./assets/lava.wav')
        lava_sound.play()
        lava_sound.fadeout(3000)


    def draw(self): # Draw cilized monkeys a bit differently
        if self.is_civilized == False:
            pygame.draw.rect(self.screen, self.colors["magenta"], self.shape_rect, border_radius=5)
        else:
            pygame.draw.rect(self.screen, self.colors["red"], self.shape_rect, border_radius=5) 


    def update(self):
        self.shape_rect = pygame.Rect(self.x,self.y,self.size,self.size)


        

