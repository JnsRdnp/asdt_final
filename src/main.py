# https://www.quora.com/Is-there-a-way-in-Python-to-dynamically-create-an-object-of-a-class-every-time-a-condition-is-met-in-a-while-loop

import pygame
import sys
from button import Button
from island import Island
import threading



class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up display
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Volcano Island')

        # Set up game variables
        self.clock = pygame.time.Clock()
        self.running = True


        self.Colors = { # Colors
            "white" : (255, 255, 255),
            "black" : (0, 0, 0),
            "blue" : (155, 210, 222),
            "yellow" : (251, 177, 60),
            "teal": (33, 131, 128),
            "magenta" : (143, 45, 86),
            "red" : (216, 17, 89)
        }

        self.island_counter = 0

        self.Islands = {} # Dictionary for Island objects
    

        self.Buttons = {} # Dictionary for Button objects


        self.create_button_objects()



    def create_island_object(self):
        self.island_counter += 1 
        self.Islands[f"island_{self.island_counter}"] = Island(self.Colors, 10, 10, 10 ,self.screen, self.Islands, f'S{self.island_counter}' ) # Create island dynamically and append to dict


    def destroy_islands(self):
        self.island_counter = 0
        for Island in self.Islands.values():
            Island.running = False

            # Killing are monkeys to ensure they dont keep on living :D
            for Monkey in Island.Monkeys_on_this_island:
                Monkey.alive=False
            for Monkey in Island.Monkeys_on_the_sea:
                Monkey.alive=False
                
        self.Islands.clear()

    def send_1_monkey_per_civilisized_island(self):
        for Island in self.Islands.values():
            # threading.Thread(target=Island.send_monkey_random()).start()
            Island.send_monkey_random_handle()

    def create_button_objects(self):
        self.Buttons["create_island"] = Button(self.Colors, self.width/3, self.height-50, 22, self.screen, onClick=self.create_island_object ,text="Tulivuori purkautuu")
        self.Buttons["wipe_island"] = Button(self.Colors, self.width/3, self.height-90, 22, self.screen, onClick=self.destroy_islands ,text="Hävitä saaret")
        self.Buttons["spread_civilization"] = Button(self.Colors, self.width/12, self.height-90, 22, self.screen, onClick=self.send_1_monkey_per_civilisized_island ,text="Levitä ilosanomaa")


    
    def process_input(self):
        """Handle input events like quitting or key presses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Kill monkeys
                self.destroy_islands()

                self.running = False


            if event.type == pygame.MOUSEBUTTONDOWN:   # Handling of button clicking
                mouse_pos = event.pos  # gets mouse position

                for Button in self.Buttons.values(): # Iterate through the buttons dictionary to find out if a button was pressed
                    if Button.button_rect.collidepoint(mouse_pos):
                        Button.on_click()


    def update(self):
        """Update game state, logic, etc."""

        if self.Islands: # Check that Islands exist 
            for Island in self.Islands.values(): # Dynamically draw each Island in the dictionary
                Island.update()
                
            # if:
            #     Island.is_island_civilized = True
            # else:
            #     Island.is_island_civilized = False

            
        if self.Buttons: # Check that Buttons exist 
            for Button in self.Buttons.values(): # Dynamically draw each Island in the dictionary
                Button.update()


    def render(self):
        """Draw everything to the screen."""
        self.screen.fill(self.Colors["blue"])  # Clear screen with white background

        
        if self.Islands: # Check that Islands exist 
            for Island in self.Islands.values(): # Dynamically draw each Island in the dictionary
                Island.draw()

        if self.Buttons: # Check that Buttons exist 
            for Button in self.Buttons.values(): # Dynamically draw each Island in the dictionary
                Button.draw()

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