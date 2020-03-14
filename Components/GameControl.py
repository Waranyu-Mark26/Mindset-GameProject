import arcade
from arcade.gui import *

WIDTH = 1280
HEIGHT = 720
Decrese = 100
Increase = 60

class PlayButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.PressUp = True
            self.pressed = False

class StopButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.PressUp = True
            self.pressed = False

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.PINK)
        self.list_output = None

        self.Move_x = 1020
        self.Move_y = 570
        self.Play = Theme()
        self.Stop = Theme()
        self.setup()

    def set_button_texturesPlay(self):
        normal = "Resources/PlayButton/play-btn-normal.png"
        hover = "Resources/PlayButton/play-btn-hover.png"
        clicked = "Resources/PlayButton/play-btn-clicked.png"
        locked = "Resources/PlayButton/play-btn-locked.png"
        self.Play.add_button_textures(normal, hover, clicked, locked)

    def set_button_texturesStop(self):
        normal = "Resources/StopButton/stop-btn-normal.png"
        hover = "Resources/StopButton/stop-btn-hover.png"
        clicked = "Resources/StopButton/stop-btn-clicked.png"
        locked = "Resources/StopButton/stop-btn-locked.png"
        self.Stop.add_button_textures(normal, hover, clicked, locked)

    def setup_theme(self):
        self.Play.set_font(24, arcade.color.WHITE)
        self.Stop.set_font(24, arcade.color.WHITE)
        self.set_button_texturesPlay()
        self.set_button_texturesStop()
    
    def on_draw(self):
        arcade.start_render()
        super().on_draw()
    
    def set_buttons(self):
        self.button_list.append(PlayButton(self, 950, 70,150,100,theme=self.Play))
        self.button_list.append(StopButton(self, 1150, 70,150,100 ,theme=self.Stop))
    
    def setup(self):
        self.setup_theme()
        self.set_buttons()




def main():
    window = arcade.Window(WIDTH, HEIGHT, "Instruction and Game Over Views Example")
    menu = MenuView()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()