import arcade
from arcade.gui import *

WIDTH = 1280
HEIGHT = 720
Decrese = 100
Increase = 60

class forwardButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.PressUp = True
            self.pressed = False

class turnleftButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.PressLeft = True
            self.pressed = False

class turnrightButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True
    def on_release(self):
        if self.pressed:
            self.game.PressRight = True
            self.pressed = False



class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.PINK)
        self.list_output = None

        self.PressUp = False
        self.PressLeft = False
        self.PressRight = False
        self.PressEnd = False
        self.list_output = arcade.SpriteList()
        self.Move_x = 1020
        self.Move_y = 570
        self.forward = Theme()
        self.turnleft = Theme()
        self.turnright = Theme()
        self.List = []
        self.setup()
    def set_button_texturesforward(self):
        normal = "Resources/Arrow/Arrow-up-normal.png"
        hover = "Resources/Arrow/Arrow-up-hover.png"
        clicked = "Resources/Arrow/Arrow-up-clicked.png"
        locked = "Resources/Arrow/Arrow-up-locked.png"
        self.forward.add_button_textures(normal, hover, clicked, locked)

    def set_button_texturesturnleft(self):
        normal = "Resources/Arrow/Arrow-turn left-normal.png"
        hover = "Resources/Arrow/Arrow-turn left-hover.png"
        clicked = "Resources/Arrow/Arrow-turn left-clicked.png"
        locked = "Resources/Arrow/Arrow-turn left-locked.png"
        self.turnleft.add_button_textures(normal, hover, clicked, locked)
        

    def set_button_texturesturnright(self):
        normal = "Resources/Arrow/Arrow-turn right-normal.png"
        hover = "Resources/Arrow/Arrow-turn right-hover.png"
        clicked = "Resources/Arrow/Arrow-turn right-clicked.png"
        locked = "Resources/Arrow/Arrow-turn right-locked.png"
        self.turnright.add_button_textures(normal, hover, clicked, locked)


    def setup_theme(self):
        self.forward.set_font(24, arcade.color.WHITE)
        self.turnleft.set_font(24, arcade.color.WHITE)
        self.turnright.set_font(24, arcade.color.WHITE)
        self.set_button_texturesforward()
        self.set_button_texturesturnleft()
        self.set_button_texturesturnright()


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lines([(980,100),(980,670)],arcade.color.RED)
        arcade.draw_lines([(30,120),(980,120)],arcade.color.RED)
        self.list_output.draw()
        super().on_draw()
    def set_buttons(self):
        self.button_list.append(forwardButton(self, 150, 70,150,100,theme=self.forward))
        self.button_list.append(turnleftButton(self, 350, 70,150,100 ,theme=self.turnleft))
        self.button_list.append(turnrightButton(self, 550, 70,150,100, theme=self.turnright))

    def setup(self):
        self.setup_theme()
        self.set_buttons()

    def on_update(self, delta_time):
        if self.PressUp:
            Button = arcade.Sprite("Resources/Arrow/Arrow-up-normal.png",scale = 0.25,center_x=self.Move_x,center_y=self.Move_y)
            self.list_output.append(Button)
            self.List.append(1)
            if self.Move_x == 1200:
                self.Move_y -= Decrese
                self.Move_x = 1020
            else:
                self.Move_x += Increase
            self.PressUp = False

        if self.PressLeft:
            Button = arcade.Sprite("Resources/Arrow/Arrow-turn left-normal.png",scale =0.25,center_x=self.Move_x,center_y=self.Move_y)
            self.list_output.append(Button)
            self.List.append(2)
            if self.Move_x == 1200:
                self.Move_y -= Decrese
                self.Move_x = 1020
            else:
                self.Move_x += Increase
            self.PressLeft = False

        if self.PressRight:
            Button = arcade.Sprite("Resources/Arrow/Arrow-turn right-normal.png",scale =0.25,center_x=self.Move_x,center_y=self.Move_y)
            self.list_output.append(Button)
            self.List.append(3)
            if self.Move_x == 1200:
                self.Move_y -= Decrese
                self.Move_x = 1020
            else:
                self.Move_x += Increase
            self.PressRight = False
        self.list_output.update()

#    def on_key_press(self,key, _modifiers):
#        if key == arcade.key.NUM_1:
#            self.PressUp = True
#        if key == arcade.key.NUM_2:
#            self.PressLeft = True
#        if key == arcade.key.NUM_3:
#            self.PressRight = True  


def main():
    window = arcade.Window(WIDTH, HEIGHT, "Instruction and Game Over Views Example")
    menu = MenuView()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()