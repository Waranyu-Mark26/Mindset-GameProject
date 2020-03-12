import arcade
from arcade.gui import *

WIDTH = 1280
HEIGHT = 720
Decrese = 150


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.TOPAZ)
        self.list_output = None
        self.PressUp = False
        self.PressLeft = False
        self.PressRight = False
        self.PressEnd = False
        self.list_output = arcade.SpriteList()
        self.Move_x = 100
        self.Move_y = 500

#    def setup(self):
#      self.list_output = arcade.SpriteList()
#       for y in range(500,40,-150):
#           for x in range(100,1010,150):
#               if self.PressUp:
#                    Button = arcade.Sprite("Resources/Arrow/Arrow-up.png",image_width=100,image_height=100,center_x=x,center_y=y)
#                    self.list_output.append(Button)
#                    self.PressUp = False
#                if self.PressLeft:
#                    Button = arcade.Sprite("Resources/Arrow/Arrow-turn left.png",image_width=100,image_height=100,center_x=x,center_y=y)
#                    self.list_output.append(Button)
#                    self.PressLeft = False
#                if self.PressRight:
#                    Button = arcade.Sprite("Resources/Arrow/Arrow-turn right.png",image_width=100,image_height=100,center_x=x,center_y=y)
#                    self.list_output.append(Button)
#                    self.PressRight = False
    def on_draw(self):
        arcade.start_render()
        self.list_output.draw()
        super().on_draw()

    def on_update(self, delta_time):
        if self.PressUp:
            Button = arcade.Sprite("Resources/Arrow/Arrow-up.png",scale = 0.5,center_x=self.Move_x,center_y=self.Move_y)
            self.list_output.append(Button)
            if self.Move_x == 1000:
                self.Move_y -= Decrese
                self.Move_x = 100
            else:
                self.Move_x += Decrese
            self.PressUp = False

        if self.PressLeft:
            Button = arcade.Sprite("Resources/Arrow/Arrow-turn left.png",scale =0.5,center_x=self.Move_x,center_y=self.Move_y)
            self.list_output.append(Button)
            if self.Move_x == 1000:
                self.Move_y -= Decrese
                self.Move_x = 100
            else:
                self.Move_x += Decrese
            self.PressLeft = False

        if self.PressRight:
            Button = arcade.Sprite("Resources/Arrow/Arrow-turn right.png",scale =0.5,center_x=self.Move_x,center_y=self.Move_y)
            self.list_output.append(Button)
            if self.Move_x == 1000:
                self.Move_y -= Decrese
                self.Move_x = 100
            else:
                self.Move_x += Decrese
            self.PressRight = False
        self.list_output.update()

    def on_key_press(self,key, _modifiers):
        if key == arcade.key.NUM_1:
            self.PressUp = True
        if key == arcade.key.NUM_2:
            self.PressLeft = True
        if key == arcade.key.NUM_3:
            self.PressRight = True  


def main():
    window = arcade.Window(WIDTH, HEIGHT, "Instruction and Game Over Views Example")
    menu = MenuView()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()