# Play, Tutorial, Credit
"""
Play --> Stage Selection --> Game
Tutorial --> Tutorial Page
Credit --> Credit Page
"""

WIDTH = 1280
HEIGHT = 720

from arcade.gui import *
import arcade
import os

class PlayButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=100, text="", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.pause = False
            self.pressed = False

class MenuView(arcade.View):

    def __init__(self):
        super().__init__()
        self.width = WIDTH
        self.height = HEIGHT

        self.background = arcade.load_texture("Resources/game-bg.jpg")

        # setup theme
        self.theme = Theme()
        self.theme.set_font(24, arcade.color.WHITE)

        # set button
        self.set_buttons()

    def on_show(self):
        arcade.set_background_color(arcade.color.TOPAZ)
        

    def on_resize(self, width=WIDTH, height=HEIGHT):
        """ This method is automatically called when the window is resized. """
        self.width,self.height = width,height

    def set_button_textures(self, dir):
        normal = f"Resources/{dir}-normal.png"
        hover = f"Resources/{dir}-hover.png"
        clicked = f"Resources/{dir}-clicked.png"
        locked = f"Resources/{dir}-locked.png"
        self.theme.add_button_textures(normal, hover, clicked, locked)

    def set_buttons(self):
        self.set_button_textures('PlayButton/play-btn')
        self.button_list.append(PlayButton(self, self.width/2, self.height/2, 150, 150,theme=self.theme))
        self.set_button_textures('TutorialButton/tutorial-btn')
        self.button_list.append(PlayButton(self, self.width/2-35, self.height/2-110, 80, 80,theme=self.theme))
        self.set_button_textures('InformationButton/information-btn')
        self.button_list.append(PlayButton(self, self.width/2+35, self.height/2-110, 80, 80,theme=self.theme))

    def on_draw(self):
        arcade.start_render()
        
        scale = (self.width) / WIDTH
        arcade.draw_lrwh_rectangle_textured(0, (self.height-HEIGHT*scale)/2,
                                            WIDTH*scale, HEIGHT*scale,
                                            self.background)

        arcade.draw_text("MENU", start_x=self.width/2, start_y=self.height/2+150,
                         color=arcade.color.DARK_BYZANTIUM, font_size=45, anchor_x="center", anchor_y="center", font_name='')

        super().on_draw()
