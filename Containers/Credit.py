import arcade

WIDTH = 1280
HEIGHT = 720


class CreditView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Members of the group Mindset",WIDTH/2,620,arcade.color.BLACK,font_size=30,anchor_x="center")
        arcade.draw_text("Mr. Traimaen Pheoemhansa 6210500528", 100, 520, arcade.color.BLACK, font_size=30)
        arcade.draw_text("Mr. Waranyu Narangsi 6210500561", 100, 390, arcade.color.BLACK, font_size=30, font_name="Arial")
        arcade.draw_text("Mr. Saranphat Janwatsiri 6210500781", 100, 260, arcade.color.BLACK, font_size=30, font_name="Arial")
        arcade.draw_text("Mr. Thitisak Siratchatamatawin 6210503551", 100, 130, arcade.color.BLACK, font_size=30, font_name="Chakra Petch")


