import arcade
import time
from Containers.MainMenu import MenuView

# from Components import Comp1
# k = Comp1.MenuView()

WIDTH = 1280
HEIGHT = 720

def main():
    window = arcade.Window(WIDTH, HEIGHT, "Algorithm Adventure", resizable=True)

    menu_view = MenuView()
    window.show_view(menu_view)
    
    arcade.run()


if __name__ == "__main__":
    main()
