import arcade
from arcade.gui import *

WIDTH = 1000
HEIGHT = 100

class Button(TextButton):
    def __init__(self, x=0, y=0, width=100, height=100, text="", theme=None, view_state=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.view_state = view_state

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False

class GameCommandPanel(arcade.View):
    def __init__(self):
        super().__init__()
        self.theme = Theme()
        self.width = 1280
        self.height = 720
        arcade.set_background_color = arcade.color.WILD_ORCHID
    
    def set_button_textures(self, dir):
        normal = f"Resources/{dir}-normal.png"
        hover = f"Resources/{dir}-hover.png"
        clicked = f"Resources/{dir}-clicked.png"
        locked = f"Resources/{dir}-locked.png"
        self.theme.add_button_textures(normal, hover, clicked, locked)

    def set_buttons(self):
        self.set_button_textures('PlayButton/play-btn')
        self.button_list.append(Button(self.width/2, self.height/2, 150, 150, theme=self.theme, view_state=1))
        self.set_button_textures('TutorialButton/tutorial-btn')
        self.button_list.append(Button(self.width/2-35, self.height/2-110, 80, 80, theme=self.theme, view_state=2))
        self.set_button_textures('InformationButton/information-btn')
        self.button_list.append(Button(self.width/2+35, self.height/2-110, 80, 80, theme=self.theme, view_state=3))
