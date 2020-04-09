import arcade
import globalvars as var
from Containers.Game import GameView
from arcade.gui import *

WIDTH = var.SCREEN_WIDTH
HEIGHT = var.SCREEN_HEIGHT

view_state_change = 0

class StageButton(TextButton):

    def __init__(self, x=0, y=0, width=180, height=180, text="1", theme=None,view=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.view = view

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            if self.view != None:
                global view_state_change
                view_state_change = self.view

class Stageview(arcade.View):

    def __init__(self, previous_window):
        super().__init__()
        self.background = arcade.load_texture("Resources/View 4.jpg")

        self.theme = Theme()
        self.theme.set_font(55, arcade.color.WHITE,font_name=('Calibri'))

        self.set_buttons()
        self.previous_window = previous_window
    
    def set_button_textures(self):
        normal = "Resources/StageSelectionButton/stage-btn-normal.png"
        hover = "Resources/StageSelectionButton/stage-btn-hover.png"
        clicked = "Resources/StageSelectionButton/stage-btn-clicked.png"
        locked = "Resources/StageSelectionButton/stage-btn-locked.png"
        self.theme.add_button_textures(normal, hover, clicked, locked)

    def set_buttons(self):
        self.set_button_textures()
        self.button_list.append(StageButton(x= 240,y= 360, theme=self.theme,view=1))
        self.button_list.append(StageButton(x= 440,y= 360,text = '2' ,theme=self.theme,view=2))
        self.button_list.append(StageButton(x= 640,y= 360,text = '3', theme=self.theme,view=3))
        self.button_list.append(StageButton(x= 840,y= 360,text = '4', theme=self.theme,view=4))
        self.button_list.append(StageButton(x= 1040,y= 360,text = '5', theme=self.theme,view=5))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,WIDTH,HEIGHT,self.background)
        if view_state_change != 0:
            game = GameView(self,view_state_change,self.previous_window)
            self.window.show_view(game)
        super().on_draw()

    def on_show(self):
        global view_state_change
        view_state_change = 0
        arcade.set_background_color(arcade.color.TOPAZ)
    
    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            menu = self.previous_window
            self.window.show_view(menu)


    

            