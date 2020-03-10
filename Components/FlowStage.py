import arcade

WIDTH = 1280
HEIGHT = 720



class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        
        self.press1 = arcade.load_texture("Resources/Arrow/Arrow-up.png")
        self.press2 = arcade.load_texture("Resources/Arrow/Arrow-turn left.png")
        self.press3 = arcade.load_texture("Resources/Arrow/Arrow-turn right.png")
        self.PressUp = False
        self.PressLeft = False
        self.PressRight = False
        self.PressEnd = False
        self.move_x = 100
        self.move_y = 500
        self.array = []

    def on_show(self):
        arcade.set_background_color(arcade.color.TOPAZ)

    def on_draw(self):
        arcade.start_render()
        
        arcade.draw_text("Plese Press 1 or 2 or 3",WIDTH/2,650,arcade.color.BLACK,24)
        super().on_draw()
        if self.PressUp:
            arcade.draw_lrwh_rectangle_textured(self.move_x,self.move_y,100,100,self.press1)
            if self.move_x == 1000:
                self.move_y -= 150
                self.move_x = 100
            else:
                self.move_x += 150
  #          self.PressUp = False
        if self.PressLeft:
            arcade.draw_lrwh_rectangle_textured(self.move_x,self.move_y,100,100,self.press2)
            if self.move_x == 1000:
                self.move_y -= 150
                self.move_x = 100
            else:
                self.move_x += 150
 #           self.PressLeft = False
        if self.PressRight:
            arcade.draw_lrwh_rectangle_textured(self.move_x,self.move_y,100,100,self.press3)
            if self.move_x == 1000:
                self.move_y -= 150
                self.move_x = 100
            else:
                self.move_x += 150
                

    def on_key_press(self,key, _modifiers):
        if key == arcade.key.NUM_1:
            self.PressUp = True
        if key == arcade.key.NUM_2:
            self.PressLeft = True
        if key == arcade.key.NUM_3:
            self.PressRight = True   
        if key == arcade.key.ENTER:
            pass




def main():
    window = arcade.Window(WIDTH, HEIGHT, "Instruction and Game Over Views Example")
    menu = MenuView()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()