# Tekstin koko https://stackoverflow.com/questions/45384910/attributeerror-pygame-surface-object-has-no-attribute-rect
# https://gamedevacademy.org/how-to-make-buttons-in-pygame-tutorial-complete-guide/#Creating_a_Basic_Button_in_Pygame
# https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
# https://stackoverflow.com/questions/25149892/how-to-get-the-width-of-text-using-pygame

import pygame

class Button():

    pygame.font.init()

    def __init__(self, colors, x,y, fontsize, screen, onClick, text=''):

        self.color = colors["black"]
        self.x = x
        self.y = y
        self.fontsize = fontsize
        self.screen = screen
        self.text = text

        self.on_click = onClick

        self.update()


    def update(self):
        self.my_font = pygame.font.SysFont('Comic Sans MS', self.fontsize)
        self.text_surface = self.my_font.render(self.text, False, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect()
        self.button_rect = pygame.Rect(self.x,self.y,self.text_rect.width+10,self.text_rect.height+2)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.button_rect, border_radius=5)
        self.screen.blit(self.text_surface, (self.button_rect.left+5, self.button_rect.top))

    # def on_click(self, function):

