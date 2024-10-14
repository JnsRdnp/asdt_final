import pygame


class Monkey():

    pygame.font.init()

    def __init__(self, colors, x, y, screen):
        
        self.color = colors["magenta"]
        self.x = x
        self.y = y
        self.screen = screen
        self.size = 7

        self.update()


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape_rect, border_radius=5)


    def update(self):
        self.shape_rect = pygame.Rect(self.x,self.y,self.size,self.size)


        

