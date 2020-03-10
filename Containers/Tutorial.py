import arcade
# import globalvars as var

WIDTH = 1280
HEIGHT = 720

class TutorialView(arcade.View):
    
    def __init__(self, previous_window):
        super().__init__()
        self.width = WIDTH
        self.height = HEIGHT

        self.background = arcade.load_texture("Resources/tutorial.png")

    def on_show(self):
        arcade.set_background_color(arcade.color.TOPAZ)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.background)
        # super.on_draw()
    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            menu = self.previous_window
            self.window.show_view(menu)
        
    
