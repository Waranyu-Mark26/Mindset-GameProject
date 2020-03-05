import arcade
import time
<<<<<<< HEAD
from Containers.Credit import CreditView
from Example.gradients import MyGame
=======
from Containers.MainMenu import MenuView
>>>>>>> 5d2d8fb96d5dda4415ddcf1f1ea0949d832bc3fc

# from Components import Comp1
# k = Comp1.MenuView()

WIDTH = 1280
HEIGHT = 720

def main():
    window = arcade.Window(WIDTH, HEIGHT, "Algorithm Adventure", resizable=True)

<<<<<<< HEAD
    menu_view = CreditView()
=======
    menu_view = MenuView()
>>>>>>> 5d2d8fb96d5dda4415ddcf1f1ea0949d832bc3fc
    window.show_view(menu_view)
    
    arcade.run()

<<<<<<< HEAD
    time.sleep(1)
    arcade.close_window()
    dwindow = MyGame(WIDTH,HEIGHT,"Hello")
    arcade.run()

=======
>>>>>>> 5d2d8fb96d5dda4415ddcf1f1ea0949d832bc3fc

if __name__ == "__main__":
    main()
