import pygame
import random

class Monkey():

    pygame.font.init()

    def __init__(self, colors, x, y, screen):
        
        self.color = colors["magenta"]
        self.x = x
        self.y = y
        self.screen = screen
        self.size = 7

        self.update()

        
    def randomize_values(self):
        self.x = random.randint(0,750)
        self.y = random.randint(0,500)
        self.fontsize = random.randint(7,50)


    def is_overlapping(self, Islands):  # Check if this Island overlaps with any islands in the dictionary
        if Islands:
            for Island in Islands.values():
                if pygame.Rect.colliderect(Island.shape_rect, self.shape_rect) == True and Island != self:
                    return True
                
            return False # If any of the islands did not overlap with this one, return False


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape_rect, border_radius=5)
        # self.screen.blit(self.text_surface, (self.shape_rect.left+self.added_size/2, self.shape_rect.top+self.added_size/2))

    def update(self):
        # self.my_font = pygame.font.SysFont('Comic Sans MS', self.fontsize)
        # self.text_surface = self.my_font.render(self.text, False, (0, 0, 0))
        # self.text_rect = self.text_surface.get_rect()
        self.shape_rect = pygame.Rect(self.x,self.y,self.size,self.size)


        

