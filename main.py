import arcade
from Containers.MainMenu import MenuView

# from Components import Comp1
# k = Comp1.MenuView()

WIDTH = 1920
HEIGHT = 1080

def main():
    window = arcade.Window(WIDTH, HEIGHT, "Algorithm Adventure")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
