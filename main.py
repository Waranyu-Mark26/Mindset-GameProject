import arcade
import time
from Containers.Credit import CreditView
from Containers.MainMenu import MenuView
from Containers.Tutorial import TutorialView

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Algorithm Adventure"

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False, fullscreen=False)
    # window = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
      
    arcade.run()

if __name__ == "__main__":
    main()
