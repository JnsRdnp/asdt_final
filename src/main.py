import pygame
import sys
from button import Button
from island import Island

class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up display
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Volcano island')

        # Set up game variables
        self.clock = pygame.time.Clock()
        self.running = True

        # Colors
        self.Colors = {
            "white" : (255, 255, 255),
            "black" : (0, 0, 0),
            "blue" : (155, 210, 222),
            "yellow" : (251, 177, 60),
            "teal": (33, 131, 128),
            "magenta" : (143, 45, 86),
            "red" : (216, 17, 89)
        }

        self.Islands = {

        }

        self.create_button_objects()

        self.create_island_object("S1", 25)



    def create_button_objects(self):
        self.Button_volcano = Button(self.Colors["black"],self.width/3, self.height-50, 22, self.screen, "Tulivuori purkautuu")

    def create_island_object(self, name, size):
        self.Island_1 = Island(self.Colors["yellow"], 100, 100, size, self.screen, name)
        self.Island_1.randomize_values() # Generate random x, y, fontsize
        self.Island_1.update() # Update to redefine the rectangle with randomized values
 
    
    def process_input(self):
        """Handle input events like quitting or key presses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Update game state, logic, etc."""
        pass

    def render(self):
        """Draw everything to the screen."""
        self.screen.fill(self.Colors["blue"])  # Clear screen with white background

        
        self.Island_1.draw()
        self.Button_volcano.draw()

        # Add any drawing code here
        pygame.display.flip()  # Update the display

    def run(self):
        """Main game loop."""
        while self.running:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(60)  # Limit the frame rate to 60 FPS

        pygame.quit()
        sys.exit()

# Start the game
if __name__ == "__main__":
    game = Game()
    game.run()