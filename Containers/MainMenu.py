# Play, Tutorial, Credit
"""
Play --> Stage Selection --> Game
Tutorial --> Tutorial Page
Credit --> Credit Page
"""

WIDTH = 1280
HEIGHT = 720

import arcade

class MenuView(arcade.View):

    def __init__(self):
        super().__init__()
        self.width = WIDTH
        self.height = HEIGHT

    def on_show(self):
        arcade.set_background_color(arcade.color.TOPAZ)
        # self.background = arcade.load_texture("Resources/game-bg.jpg")

    def on_resize(self, width=WIDTH, height=HEIGHT):
        """ This method is automatically called when the window is resized. """
        
        # print(f"Window resized to: {width}, {height}")
        self.width,self.height = width,height

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Main Menu", start_x=self.width/2, start_y=self.height/2+100,
                         color=arcade.color.BLACK, font_size=30, anchor_x="center")