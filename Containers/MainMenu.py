# Play, Tutorial, Credit
"""
Play --> Stage Selection --> Game
Tutorial --> Tutorial Page
Credit --> Credit Page
"""

WIDTH = 1920
HEIGHT = 1080

import arcade

class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.TOPAZ)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Our first page!!", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

