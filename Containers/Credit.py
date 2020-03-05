import arcade

WIDTH = 1280
HEIGHT = 720


class CreditView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Mr. Traimaen Pheoemhansa 6210500528", WIDTH / 2, HEIGHT / 2, arcade.color.BLACK, font_size=50,
                         anchor_x="left",anchor_y="center")
        arcade.draw_text("MR Warunyu Narungsri", 640, 360, arcade.color.BLACK, font_size=30,anchor_x="left",anchor_y="top")
        arcade.draw_text_2("Mr Traiman Phemhansa",WIDTH/2,HEIGHT/2,arcade.color.BLACK,font_size=12,anchor_x="center",anchor_y="top")
