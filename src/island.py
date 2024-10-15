# https://gamedevacademy.org/how-to-make-buttons-in-pygame-tutorial-complete-guide/#Creating_a_Basic_Button_in_Pygame
# https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
# https://stackoverflow.com/questions/25149892/how-to-get-the-width-of-text-using-pygame
# Tekstin koko https://stackoverflow.com/questions/45384910/attributeerror-pygame-surface-object-has-no-attribute-rect
# Overlapping rectangles https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect

import pygame
import random
from monkey import Monkey
import threading


class Island():

    pygame.font.init()

    def __init__(self, colors, x, y, fontsize, screen, Islands, text=''):
        
        self.color = colors["yellow"]
        self.color_dict = colors
        self.x = x
        self.y = y
        self.fontsize = fontsize
        self.screen = screen
        self.text = text
        self.Islands = Islands


        self.added_size = 20 # For the island padding relative to text
        
        

        self.Monkeys_on_this_island={

        }
        self.monkey_count = 0
        
        self.update()
        self.initialize_island()
        self.create_monkeys()
        self.island_creation_sound()


        if self.text == 'S1':  # Civilize island isntanly if this is ISLAND 1
            self.monkeys_civilize()

        
    def monkeys_civilize(self): # Civilize all monkeys on this island

        for monkey_key in list(self.Monkeys_on_this_island.keys()): 
            monkey = self.Monkeys_on_this_island[monkey_key]
            monkey.is_civilized = True


    def island_creation_sound(self):
        lava_sound = pygame.mixer.Sound('./assets/lava.wav')
        lava_sound.play()
        lava_sound.fadeout(3000)


    def initialize_island(self):
        while True: # Recreate the values for Island till there is no overlap
            self.randomize_values()  # Generate random x, y, fontsize
            self.update()  # Update to redefine the rectangle with randomized values

            if self.is_overlapping() == False or self.is_overlapping() == None:
                break  # Exit the loop succesfully if no overlap is found
            


    def create_monkeys(self):
        # monkey_index = 0
        
        for monkey_index in range(0,10):
            monkey_loc = self.generate_random_location_for_monkey()
            self.Monkeys_on_this_island[f"monkey_{monkey_index}"] = Monkey(self.color_dict, monkey_loc[0], monkey_loc[1], self.screen)


    def generate_random_location_for_monkey(self):
        max_monkey_location = self.shape_rect.bottomright
        min_monkey_location = self.shape_rect.topleft

        random_monkey_x = random.randint(min_monkey_location[0]+7, max_monkey_location[0]-7) # 7, because diameter of monkeys is 7 and we dont want it overflow the island
        random_monkey_y = random.randint(min_monkey_location[1]+7, max_monkey_location[1]-7)

        random_monkey_location = (random_monkey_x, random_monkey_y)

        return random_monkey_location
        


    def randomize_values(self):
        self.x = random.randint(0,725)
        self.y = random.randint(0,500)
        self.fontsize = random.randint(7,50)


    def is_overlapping(self):  # Check if this Island overlaps with any islands in the dictionary
        if self.Islands:
            for Island in self.Islands.values():
                if pygame.Rect.colliderect(Island.shape_rect, self.shape_rect) == True and Island != self:
                    return True
                
            return False # If any of the islands did not overlap with this one, return False
        

    def count_monkeys(self):
        value = len(self.Monkeys_on_this_island)
        return value


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape_rect, border_radius=5)

        if self.Monkeys_on_this_island:
            for Monkey in self.Monkeys_on_this_island.values():
                Monkey.draw()

        self.screen.blit(self.text_surface, (self.shape_rect.left+self.added_size/2, self.shape_rect.top+self.added_size/2))
        

    def update(self):
        if self.Monkeys_on_this_island: # " By iterating over list(self.Monkeys_on_this_island.keys()), you avoid modifying the dictionary while iterating "
            
            for monkey_key in list(self.Monkeys_on_this_island.keys()): # We use list to be able to delete iterated item from list
                monkey = self.Monkeys_on_this_island[monkey_key]
                monkey.update()
                if not monkey.alive:
                    del self.Monkeys_on_this_island[monkey_key]
        
        self.monkey_count = self.count_monkeys() # Update the monkey count here to ensure new information
        
        self.my_font = pygame.font.SysFont('Comic Sans MS', self.fontsize)
        self.text_surface = self.my_font.render(f'{self.text}:{self.monkey_count}', False, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.shape_rect = pygame.Rect(self.x,self.y,self.text_rect.width+self.added_size,self.text_rect.height+self.added_size)


        

