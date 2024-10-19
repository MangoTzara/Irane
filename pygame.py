"""
Platformer Game
"""
import math
import arcade
# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Whatever"


class MyGame(arcade.Window):
    start_x = 0
    finish_x = 100
    speed_x = 1
    """
    Main application class.
    """

    
    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        
        pass

    def on_draw(self):
        """Render the screen."""
        
        self.clear()
        arcade.draw_parabola_outline(self.start_x,0,self.finish_x,100, arcade.csscolor.RED,10 )
        self.start_x += self.speed_x 
        self.finish_x += self.speed_x 
        

def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
