import arcade
import time
from Containers.Credit import CreditView
from Containers.MainMenu import MenuView

# from Components import Comp1    
# k = Comp1.MenuView()

WIDTH = 1280   
HEIGHT = 720

def main():
    window = arcade.Window(WIDTH, HEIGHT, "Algorithm Adventure", resizable=False, fullscreen=False)

    menu_view = MenuView()
    window.show_view(menu_view)
      
    arcade.run()


if __name__ == "__main__":
    main()
