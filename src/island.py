# https://gamedevacademy.org/how-to-make-buttons-in-pygame-tutorial-complete-guide/#Creating_a_Basic_Button_in_Pygame
# https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
# https://stackoverflow.com/questions/25149892/how-to-get-the-width-of-text-using-pygame
# Tekstin koko https://stackoverflow.com/questions/45384910/attributeerror-pygame-surface-object-has-no-attribute-rect
# Overlapping rectangles https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect

import pygame
import random
from monkey import Monkey
import threading
import time
from threading import Semaphore


class Island():

    pygame.font.init()

    def __init__(self, colors, x, y, fontsize, screen, Islands, text=''):
        
        self.color = colors["yellow"]
        self.platform_color = colors["white"]
        self.color_dict = colors
        self.x = x
        self.y = y
        self.fontsize = fontsize
        self.screen = screen
        self.text = text
        self.Islands = Islands


        self.added_size = 10 # For the island padding relative to text
        self.is_island_civilized = False        
        

        self.Monkeys_on_this_island=[]
        self.Monkeys_on_the_sea=[]

        self.monkey_count = 0

        self.Platforms = {}
        
        self.update()
        self.initialize_island()
        self.create_monkeys()
        self.island_creation_sound()

        self.automatic_sender = True

        self.mutex = Semaphore(1)

        self.Running = True

        if self.text == 'S1':  # Civilize island isntanly if this is ISLAND 1
            self.monkeys_civilize()

        # self.toggle_automatic_monkey_sender()
        automatic_handle = threading.Thread(target=self.toggle_automatic_monkey_sender)
        automatic_handle.start()


    def toggle_automatic_monkey_sender(self):

        while self.Running == True:
            while self.automatic_sender and self.Running and self.is_island_civilized:
                self.send_monkey_random_handle()
                time.sleep(10)
            time.sleep(1)



    def send_monkey_random_handle(self):
        handle = threading.Thread(target=self.send_monkey_random)
        handle.start()

    def positivenegative_random(self):
        positive_or_negative = random.randint(0,1)
        return positive_or_negative
    
    def axis_random(self):
        vertical_or_horizontal = random.randint(0,1)
        return vertical_or_horizontal

    def send_monkey_random(self):

        posneg = self.positivenegative_random()
        axis = self.axis_random()
        # monkey_is_on_sea = True
        run = True

        if len(self.Monkeys_on_this_island)>0 and self.is_island_civilized:
            # Create a copy of the values to avoid modifying the dictionary during iteration
            for Monkey in list(self.Monkeys_on_this_island):

                self.Monkeys_on_the_sea.append(Monkey)

                self.Monkeys_on_this_island.remove(Monkey)

                # self.Monkeys_on_this_island
                while run == True and Monkey.alive and self.Running==True:

                    for Island in self.Islands.values(): # Check if monkey is on any of islands and change the land state based on that
                        if not pygame.Rect.colliderect(Monkey.shape_rect, Island.shape_rect):
                            Monkey.is_on_land = False
                            break
                        Monkey.is_on_land = True

                    if posneg == 0 and axis == 0:
                        Monkey.x += 7
                    elif posneg == 1 and axis == 0:
                        Monkey.x -= 7
                    elif posneg == 0 and axis == 1:
                        Monkey.y += 7
                    elif posneg == 1 and axis == 1:
                        Monkey.y -= 7


                    for Island in self.Islands.values():

                        if pygame.Rect.colliderect(Monkey.shape_rect, Island.shape_rect) and Island != self:

                            with self.mutex:
                                Island.Monkeys_on_this_island.append(Monkey)
                                # self.Monkeys_on_the_sea.remove(Monkey)
                            run = False
                            break  # Stop checking other islands once a match is found

                    time.sleep(0.1) 


                if Monkey.alive == False:
                    break

                if run == False:
                    break
                        

                
                    


    def monkeys_civilize(self):
        for Monkey in self.Monkeys_on_this_island: 
            Monkey.is_civilized = True # Civilize the monkeys

        # self.is_island_civilized = True # Mark island as civilisized


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
        # Create 10 monkeys and add them to the list
        for monkey_index in range(10):
            monkey_loc = self.generate_random_location_for_monkey()
            # Append Monkey objects directly to the list
            self.Monkeys_on_this_island.append(Monkey(self.color_dict, monkey_loc[0], monkey_loc[1], self.screen, self.Islands))


    def generate_random_location_for_monkey(self):
        max_monkey_location = self.shape_rect.bottomright
        min_monkey_location = self.shape_rect.topleft

        random_monkey_x = random.randint(min_monkey_location[0]+7, max_monkey_location[0]-14) # 7, because diameter of monkeys is 7 and we dont want it overflow the island
        random_monkey_y = random.randint(min_monkey_location[1]+7, max_monkey_location[1]-14)

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
        return f"{value:02}" # Return as zero-padded


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape_rect, border_radius=5)

        if self.is_island_civilized: # Draw platforms if is civ...
            for platform in self.Platforms.values():
                pygame.draw.rect(self.screen, self.platform_color, platform, border_radius=2)

        if self.Monkeys_on_this_island:
            for Monkey in self.Monkeys_on_this_island:
                Monkey.draw()

        if self.Monkeys_on_the_sea:
            for Monkey in self.Monkeys_on_the_sea:
                Monkey.draw()

        self.screen.blit(self.text_surface, (self.shape_rect.left+self.added_size/2, self.shape_rect.top+self.added_size/2))
        

    def check_if_any_civilisized_monkeys(self):
        for Monkey in self.Monkeys_on_this_island:
            if Monkey.is_civilized == True:
                return True
            
        return False
        

    def update(self):
        if self.Monkeys_on_this_island: # " By iterating over list(self.Monkeys_on_this_island.keys()), you avoid modifying the dictionary while iterating "
            with self.mutex:
                for Monkey in list(self.Monkeys_on_this_island): # We use list to be able to delete iterated item from list
                    Monkey.update()
                    if not Monkey.alive:
                        self.Monkeys_on_this_island.remove(Monkey)

        if self.Monkeys_on_the_sea:
            with self.mutex:
                for Monkey in list(self.Monkeys_on_the_sea): # We use list to be able to delete iterated item from list
                    Monkey.update()
                    if not Monkey.alive:
                        self.Monkeys_on_the_sea.remove(Monkey)
            
        
        self.monkey_count = self.count_monkeys() # Update the monkey count here to ensure new information

        if self.check_if_any_civilisized_monkeys() == True and self.is_island_civilized == False: # If any monkey is civ then island is too
            self.monkeys_civilize() # Civilize every other monkey too
            self.is_island_civilized=True
        
        self.my_font = pygame.font.SysFont('Comic Sans MS', self.fontsize)
        self.text_surface = self.my_font.render(f'{self.text}:{self.monkey_count}', False, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.shape_rect = pygame.Rect(self.x,self.y,self.text_rect.width+self.added_size,self.text_rect.height+self.added_size)

        self.define_platforms() # Define the possible platforms for if island civilisizes


    def define_platforms(self):
        # Right
        self.Platforms['platform_rect_right'] = pygame.Rect(self.shape_rect.right, self.shape_rect.centery-(self.shape_rect.height/10), self.shape_rect.width/5, self.shape_rect.height/5)
        
        # Left
        self.Platforms['platform_rect_left'] = pygame.Rect(self.shape_rect.left-self.shape_rect.width/5, self.shape_rect.centery-(self.shape_rect.height/10), self.shape_rect.width/5, self.shape_rect.height/5)

        # Top
        self.Platforms['platform_rect_top'] = pygame.Rect((self.shape_rect.centerx-(self.shape_rect.width/10), self.shape_rect.top-self.shape_rect.height/4, self.shape_rect.width/6, self.shape_rect.height/4)) 

        # Bottom
        self.Platforms['platform_rect_bottom'] = pygame.Rect((self.shape_rect.centerx-(self.shape_rect.width/10), self.shape_rect.bottom, self.shape_rect.width/6, self.shape_rect.height/4)) 

