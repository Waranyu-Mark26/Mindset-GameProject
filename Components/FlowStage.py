import arcade

WIDTH = 1280
HEIGHT = 720

move_x = 30
move_y = 600

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        
        self.press1 = arcade.load_texture("Resources/Arrow/Arrow-up.png")
        self.press2 = arcade.load_texture("Resources/Arrow/Arrow-turn left.png")
        self.press3 = arcade.load_texture("Resources/Arrow/Arrow-turn right.png")

    def on_show(self):
        arcade.set_background_color(arcade.color.TOPAZ)

    def on_draw(self):
        arcade.start_render()
        
        arcade.draw_text("Plese Press 1 or 2 or 3",WIDTH/2,650,arcade.color.BLACK,24)
        super().on_draw()


#    def on_key_press(self, _x, _y, _button, _modifiers):
#        while True:
#           if key == arcade.key.NUM_1:
#                arcade.draw_lrwh_rectangle_textured(30,600,150,50,self.press1)
#            elif key == arcade.key.NUM_2:
#                arcade.draw_lrwh_rectangle_textured(30,600,150,50,self.press1)
#            elif key == arcade.key.NUM_3:
#                arcade.draw_lrwh_rectangle_textured(30,600,150,50,self.press1)    
#            elif key == arcade.key.ENTER:
#                pass



def main():
    window = arcade.Window(WIDTH, HEIGHT, "Instruction and Game Over Views Example")
    menu = MenuView()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()