import arcade

WIDTH = 1280
HEIGHT = 720

class Stageview(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = arcade.load_texture("Resources/game-bg.jpg")
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,WIDTH,HEIGHT,self.background)
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

