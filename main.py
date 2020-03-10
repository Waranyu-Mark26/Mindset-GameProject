import arcade
from Containers.Credit import CreditView
from Containers.MainMenu import MenuView
from Containers.Tutorial import TutorialView
import globalvars as var

SCREEN_WIDTH = var.SCREEN_WIDTH
SCREEN_HEIGHT = var.SCREEN_HEIGHT
SCREEN_TITLE = "Algorithm Adventure"

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False, fullscreen=False)
    # window = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)

    arcade.run()

if __name__ == "__main__":
    main()
