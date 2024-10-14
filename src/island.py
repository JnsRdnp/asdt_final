# https://gamedevacademy.org/how-to-make-buttons-in-pygame-tutorial-complete-guide/#Creating_a_Basic_Button_in_Pygame
# https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
# https://stackoverflow.com/questions/25149892/how-to-get-the-width-of-text-using-pygame
# Tekstin koko https://stackoverflow.com/questions/45384910/attributeerror-pygame-surface-object-has-no-attribute-rect

import pygame
import random

class Island():

    pygame.font.init()

    def __init__(self, color, x, y, fontsize, screen,text=''):
        
        self.color = color
        self.x = x
        self.y = y
        self.fontsize = fontsize
        self.screen = screen
        self.text = text

        self.added_size = 20 # For the island padding relative to text

        self.update()

        
    def randomize_values(self):
        self.x = random.randint(50,750)
        self.y = random.randint(50,550)
        self.fontsize = random.randint(3,50)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.button_rect, border_radius=5)
        self.screen.blit(self.text_surface, (self.button_rect.left+self.added_size/2, self.button_rect.top+self.added_size/2))

    def update(self):
        self.my_font = pygame.font.SysFont('Comic Sans MS', self.fontsize)
        self.text_surface = self.my_font.render(self.text, False, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.button_rect = pygame.Rect(self.x,self.y,self.text_rect.width+self.added_size,self.text_rect.height+self.added_size)


        

