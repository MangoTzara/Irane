"""
Platformer Game
"""
import arcade
# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Whatever"


class MyGame(arcade.Window):
    tick = 0
    x = 0
    y = 0
    speed_x = 2
    speed_y = 1
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
        
        arcade.draw_circle_filled(self.x,self.y,73,arcade.color.RED)
        if self.x + self.speed_x < 0 or  self.x + self.speed_x >  SCREEN_WIDTH:
            self.speed_x *= -1
        if self.y + self.speed_y < 0 or  self.y + self.speed_y >  SCREEN_HEIGHT:
            self.speed_y *= -1

        self.x += self.speed_x
        self.y += self.speed_y        
        self.tick += 1

def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
