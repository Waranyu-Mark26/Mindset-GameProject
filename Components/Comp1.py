import arcade

WIDTH = 1920
HEIGHT = 1080

class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Menu Screen - click to advance", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # game_view = GameView()
        # game_view.setup()
        # self.window.show_view(game_view)
        print('Hello World')