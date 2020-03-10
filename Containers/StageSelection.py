from arcade.gui import *
import arcade
# from Containers.MainMenu import MenuView

WIDTH = 1280
HEIGHT = 720

class StageButton(TextButton):

    def __init__(self, x=0, y=0, width=180, height=180, text="1", theme=None,view=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.view = view

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            print(self.view)
            if self.view != None:
                pass

class Stageview(arcade.View):

    def __init__(self, previous_window):
        super().__init__()
        self.background = arcade.load_texture("Resources/View 4.jpg")

        self.theme = Theme()
        self.theme.set_font(55, arcade.color.WHITE,font_name=('Calibri'))

        self.set_buttons()
        self.previous_window = previous_window
    
    def set_button_textures(self):
        normal = "Resources/StageSelectionButton/StageButton.png"
        hover = "Resources/StageSelectionButton/StageButton.png"
        clicked = "Resources/StageSelectionButton/StageButton.png"
        locked = "Resources/StageSelectionButton/StageButton.png"
        self.theme.add_button_textures(normal, hover, clicked, locked)

    def set_buttons(self):
        self.set_button_textures()
        self.button_list.append(StageButton(120, 360, theme=self.theme))
        self.button_list.append(StageButton(320, 360,text = '2' ,theme=self.theme))
        self.button_list.append(StageButton(520, 360,text = '3', theme=self.theme))
        self.button_list.append(StageButton(720, 360,text = '4', theme=self.theme))
        self.button_list.append(StageButton(920, 360,text = '5', theme=self.theme))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,WIDTH,HEIGHT,self.background)
        super().on_draw()

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
    
    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            menu = self.previous_window
            self.window.show_view(menu)