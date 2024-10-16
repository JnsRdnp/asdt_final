import pygame
from toneplayer import Note
import time
import random
# from pygame.mixer import pre_init
import threading


class Monkey():
    pygame.font.init()

    def __init__(self, colors, x, y, screen, Islands):
        pygame.mixer.init(frequency=44100, size=-16, channels=1)

        self.colors = colors
        self.x = x
        self.y = y
        self.screen = screen
        self.size = 7
        self.Islands = Islands

        self.update()

        self.is_on_land = True # Value to watch to know surviving possibility

        self.alive = True # If this turns to false, this monkey is removed from the monkey list it is currently in

        self.is_civilized = False # Can this monkey civilize other monkeys

        self.laugh_sound = pygame.mixer.Sound('./assets/laugh.wav')
        self.shark_sound = pygame.mixer.Sound('./assets/chomp.wav')

        # threading.Thread(target=self.play_random_sound).start() # Commented out due to ear failure

        dying_handle = threading.Thread(target=self.die)
        dying_handle.start()

    def die(self): # Function to possibly die due to laughter or getting eaten by shark

        while self.alive:
            
            while self.is_on_land and self.alive:
                random_integer = random.randint(1,100)
                for i in range(10): # Sleep 10 seconds but in for loop to avoid to long sleep times
                    time.sleep(1)
                    if self.is_on_land == False or self.alive == False: 
                        break
                if random_integer == 50:
                    self.laugh_sound.play()
                    print("Apina kuoli nauruun")
                    self.alive = False


            while self.is_on_land == False and self.alive:
                random_integer = random.randint(1,100)
                time.sleep(1)
                if random_integer == 50:
                    self.shark_sound.play()
                    print("Apina kuoli merelle")
                    self.alive = False
            
      



    def play_random_sound(self):
        while self.alive == True:
            random_hz = random.randint(400,2000)
            Beep = Note(random_hz)
            Beep.play(-1)
            time.sleep(1)
            Beep.stop()
            time.sleep(10)


    def draw(self): # Draw cilized monkeys a bit differently
        if self.is_civilized == False:
            pygame.draw.rect(self.screen, self.colors["magenta"], self.shape_rect, border_radius=5)
        else:
            pygame.draw.rect(self.screen, self.colors["red"], self.shape_rect, border_radius=5) 


    def update(self):
        self.shape_rect = pygame.Rect(self.x,self.y,self.size,self.size)


        

