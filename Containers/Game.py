import arcade
from Components.GameCommand import GameCommandPanel
import globalvars as var
from arcade.gui import *

WIDTH = var.SCREEN_WIDTH
HEIGHT = var.SCREEN_HEIGHT

# Game Button
space_y = 60
space_X = 60
start_x = 1020
start_y = 570
max_x_panel = 1200

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.AMAZON)
        self.background = arcade.load_texture("Resources/game-bg2.jpg")
        # If you have sprite lists, you should create them here,
        # and set them to None

        self.list_output = None
        self.PressUp = False
        self.PressLeft = False
        self.PressRight = False
        self.PressEnd = False
        self.list_output = arcade.SpriteList()
        self.Move_x = start_x
        self.Move_y = start_y
        self.forward = Theme()
        self.turnleft = Theme()
        self.turnright = Theme()
        self.List = []
        self.setup()

    def set_button_texturesforward(self):
        normal = "Resources/Arrow/Arrow-up.png"
        hover = "Resources/Arrow/Arrow-up.png"
        clicked = "Resources/Arrow/Arrow-up.png"
        locked = "Resources/Arrow/Arrow-up.png"
        self.forward.add_button_textures(normal, hover, clicked, locked)

    def set_button_texturesturnleft(self):
        normal = "Resources/Arrow/Arrow-turn left.png"
        hover = "Resources/Arrow/Arrow-turn left.png"
        clicked = "Resources/Arrow/Arrow-turn left.png"
        locked = "Resources/Arrow/Arrow-turn left.png"
        self.turnleft.add_button_textures(normal, hover, clicked, locked)
        

    def set_button_texturesturnright(self):
        normal = "Resources/Arrow/Arrow-turn right.png"
        hover = "Resources/Arrow/Arrow-turn right.png"
        clicked = "Resources/Arrow/Arrow-turn right.png"
        locked = "Resources/Arrow/Arrow-turn right.png"
        self.turnright.add_button_textures(normal, hover, clicked, locked)

    def setup_theme(self):
        self.forward.set_font(24, arcade.color.WHITE)
        self.turnleft.set_font(24, arcade.color.WHITE)
        self.turnright.set_font(24, arcade.color.WHITE)
        self.set_button_texturesforward()
        self.set_button_texturesturnleft()
        self.set_button_texturesturnright()

    def set_buttons(self):
        self.button_list.append(forwardButton(self, 150, 70,150,150,theme=self.forward))
        self.button_list.append(turnleftButton(self, 350, 70,150,150 ,theme=self.turnleft))
        self.button_list.append(turnrightButton(self, 550, 70,150,150, theme=self.turnright))

    def setup(self):
        # Create your sprites and sprite lists here
        self.setup_theme()
        self.set_buttons()

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        
        # Draw background
        arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.background)

        # Draw Flow Stage
        self.list_output.draw()

        # Draw outline
        start_y = 0
        start_x = 0
        width = 1000
        height = 100
        arcade.draw_lrtb_rectangle_outline(start_x, start_x + width,
                                           start_y + height, start_y,
                                           arcade.color.WHITE, 1)
        
        start_y = 100
        start_x = 0
        width = 1000
        height = 620
        arcade.draw_lrtb_rectangle_outline(start_x, start_x + width,
                                           start_y + height, start_y,
                                           arcade.color.WHITE, 1)
        
        start_y = 0
        start_x = 1000
        width = 280
        height = 200
        arcade.draw_lrtb_rectangle_outline(start_x, start_x + width,
                                           start_y + height, start_y,
                                           arcade.color.WHITE, 1)

        super().on_draw()
        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if self.PressUp:
            Button = arcade.Sprite("Resources/Arrow/Arrow-up.png",scale=0.25,center_x=self.Move_x,center_y=self.Move_y)
            self.list_output.append(Button)
            self.List.append(1)
            if self.Move_x == max_x_panel:
                self.Move_y -= space_y
                self.Move_x = start_x
            else:
                self.Move_x += space_X
            self.PressUp = False

        if self.PressLeft:
            Button = arcade.Sprite("Resources/Arrow/Arrow-turn left.png",scale=0.25,center_x=self.Move_x,center_y=self.Move_y)
            self.list_output.append(Button)
            self.List.append(2)
            if self.Move_x == max_x_panel:
                self.Move_y -= space_y
                self.Move_x = start_x
            else:
                self.Move_x += space_X
            self.PressLeft = False

        if self.PressRight:
            Button = arcade.Sprite("Resources/Arrow/Arrow-turn right.png",scale=0.25,center_x=self.Move_x,center_y=self.Move_y)
            self.list_output.append(Button)
            self.List.append(3)
            if self.Move_x == max_x_panel:
                self.Move_y -= space_y
                self.Move_x = start_x
            else:
                self.Move_x += space_X
            self.PressRight = False

        self.list_output.update()

class forwardButton(TextButton):
    def __init__(self, game, x=0, y=0, width=50, height=50, text="", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.PressUp = True
            self.pressed = False

class turnleftButton(TextButton):
    def __init__(self, game, x=0, y=0, width=50, height=50, text="", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.PressLeft = True
            self.pressed = False

class turnrightButton(TextButton):
    def __init__(self, game, x=0, y=0, width=50, height=50, text="", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True
    def on_release(self):
        if self.pressed:
            self.game.PressRight = True
            self.pressed = False