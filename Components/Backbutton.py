from arcade.gui import *
import arcade

WIDTH = 1280
HEIGHT = 720


class PlayButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40,text="", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.pause = False
            self.pressed = False

class CreditView(arcade.View):

    def __init__(self):
        super().__init__()
        self.theme = Theme()
        self.set_buttons()
        self.theme.set_font(24, arcade.color.WHITE)
        
        

    def on_draw(self):
        arcade.start_render()
        super().on_draw()

    def on_show(self):
        arcade.set_background_color(arcade.color.TOPAZ)


    def set_button_textures(self, dir):
        normal = f"resources/HomeButton/{dir}-noemal.png"
        hover = f"resources/HomeButton/{dir}-hover.png"
        clicked = f"resources/HomeButton/{dir}-clicked.png"
        locked = f"resources/HomeButton/{dir}-locked.png"
        self.theme.add_button_textures(normal, hover, clicked, locked)

    def set_buttons(self):
        self.set_button_textures('HomeButton/play-btn')
        self.button_list.append(PlayButton(self, WIDTH/2, HEIGHT/2, 150, 50, theme=self.theme))


