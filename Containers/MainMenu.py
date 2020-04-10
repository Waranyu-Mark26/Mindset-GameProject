from arcade.gui import *
from Containers.StageSelection import Stageview
from Containers.Tutorial import TutorialView
from Containers.Credit import CreditView
import arcade
import globalvars as var

WIDTH = var.SCREEN_WIDTH
HEIGHT = var.SCREEN_HEIGHT

view_state_change = 0
# 0 : MainMenu
# 1 : StageView
# 2 : TutorialView
# 3 : CreditView

class Button(TextButton):
    def __init__(self, x=0, y=0, width=100, height=100, text="", theme=None, view_state=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.view_state = view_state

    def on_press(self):
        self.pressed = True

    def on_mouse_hover(self):
        self.hover = True

    def on_release(self):
        if self.pressed:
            self.pressed = False

            # print(self.view_state)
            if self.view_state != None:
                global view_state_change
                view_state_change = self.view_state

class MenuView(arcade.View):
    
    def __init__(self):
        super().__init__()
        self.width = WIDTH
        self.height = HEIGHT
        self.background = arcade.load_texture("Resources/game-bg.jpg")
        
        # setup theme
        self.theme = Theme()
        self.theme.set_font(24, arcade.color.WHITE)

        # set button
        self.set_buttons()

    def on_show(self):
        global view_state_change
        view_state_change = 0
        arcade.set_background_color(arcade.color.TOPAZ)

    def on_resize(self, width=WIDTH, height=HEIGHT):
        """ This method is automatically called when the window is resized. """
        self.width,self.height = width,height

    def set_button_textures(self, dir):
        normal = f"Resources/{dir}-normal.png"
        hover = f"Resources/{dir}-hover.png"
        clicked = f"Resources/{dir}-clicked.png"
        locked = f"Resources/{dir}-locked.png"
        self.theme.add_button_textures(normal, hover, clicked, locked)

    def set_buttons(self):
        self.set_button_textures('PlayButton/play-btn')
        self.button_list.append(Button(self.width/2, self.height/2, 150, 150, theme=self.theme, view_state=1))
        self.set_button_textures('TutorialButton/tutorial-btn')
        self.button_list.append(Button(self.width/2-35, self.height/2-110, 80, 80, theme=self.theme, view_state=2))
        self.set_button_textures('InformationButton/information-btn')
        self.button_list.append(Button(self.width/2+35, self.height/2-110, 80, 80, theme=self.theme, view_state=3))

    def on_draw(self):
        arcade.start_render()

        scale = (self.width) / WIDTH
        arcade.draw_lrwh_rectangle_textured(0, (self.height-HEIGHT*scale)/2,
                                            WIDTH*scale, HEIGHT*scale,
                                            self.background)

        # arcade.draw_text("MENU", start_x=self.width/2, start_y=self.height/2+120,
        #                  color=arcade.color.DARK_BYZANTIUM, font_size=40, anchor_x="center", anchor_y="center", font_name='Arial', bold=True)

        arcade.draw_text("Algorithm Adventure", start_x=self.width/2, start_y=self.height/2+140,
                         color=arcade.color.DARK_SCARLET, font_size=70, anchor_x="center", anchor_y="center", font_name='Arial', bold=True)
        
        if view_state_change == 1:
            stage = Stageview(self)
            # game = GameView(self,1)
            self.window.show_view(stage)
        elif view_state_change == 2:
            tutorial = TutorialView(self)
            self.window.show_view(tutorial)
        elif view_state_change == 3:
            credit = CreditView(self)
            self.window.show_view(credit)

        super().on_draw()
        