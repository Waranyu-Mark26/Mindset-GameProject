from arcade.gui import *
import arcade
#from Containers.MainMenu import MenuView
#from Containers.Tutorial import TutorialView

WIDTH = 1280
HEIGHT = 720

class LoseOrWinView(arcade.View):
    def __init__(self,loseorwin,level = 1):
        super().__init__()
        self.loseorwin = loseorwin
        self.other = Theme()
        self.mainmenu = Theme()
        self.stage = Theme()
        self.other.set_font(30,arcade.color.WHITE,font_name=('Arial'))
        self.newlevel = level
        self.set_buttons()
        arcade.set_background_color(arcade.color.AMAZON)

        #setBackground
        if self.loseorwin == "Lose":
            self.background = arcade.load_texture("Resources/View3.png")
        elif self.loseorwin == "Win":
            self.background = arcade.load_texture("Resources/game-bg3.png")
    
    def set_button_texturesother(self):
        normal = "Resources/OtherButton/other-btn-normal.png"
        hover = "Resources/OtherButton/other-btn-normal.png"
        clicked = "Resources/OtherButton/other-btn-normal.png"
        locked = "Resources/OtherButton/other-btn-normal.png"
        self.other.add_button_textures(normal,hover,clicked,locked)
    
    def set_buttons(self):
        self.set_button_texturesother()
        if self.loseorwin == "Lose":
            self.button_list.append(Button(x=640,y=430,text='TRY AGAIN',theme= self.other,view= self.newlevel,game=self))
            self.button_list.append(Button(x=640,y=280,text='MAIN MENU',theme= self.other,view= 0,game=self))
        elif self.loseorwin == "Win":
            self.button_list.append(Button(x=640,y=430,text='NEXT LEVEL',theme= self.other,view= self.newlevel+1,game=self))
            self.button_list.append(Button(x=640,y=280,text='TRY AGAIN',theme= self.other,view= self.newlevel,game=self))
            self.button_list.append(Button(x=640,y=130,text='MAIN MENU',theme= self.other,view= 0,game=self))



    #def on_key_press(self, key, _modifiers):
       # if self.loseorwin == "Lose":

    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.background)
        if self.loseorwin == 'Lose':
            text = "YOU LOSE !!"
            fcolor = arcade.color.RED_DEVIL
        elif self.loseorwin == 'Win':
            text = "YOU WIN !!"
            fcolor = arcade.color.GOLDEN_YELLOW
        arcade.draw_text(text, start_x=640, start_y=590,
                         color=fcolor, font_size=100, anchor_x="center", anchor_y="center", font_name='Calibri', bold=True)
        super().on_draw()

class Button(TextButton):
    def __init__(self, x=0, y=0, width=400, height=115, text="", theme=None,view=None,game=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.view = view
        self.text = text

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            
            if self.view != None:
                if self.view == 0:
                    print('KUY')
                    menu = Menu.MenuView()
                elif 1 <= self.view <= 5:
                    if self.text == 'TRY AGAIN':
                        menu = GameView(Stageview(MenuView()),self.view)
                    elif self.text == 'NEXT LEVEL':
                        menu = GameView(Stageview(MenuView()),self.view+1)
                elif self.view > 5:
                    menu = Stageview(MenuView())
                self.game.window.show_view(menu)
                



SCREEN_TITLE = 'TEST'
def main():
    window = arcade.Window(WIDTH, HEIGHT, SCREEN_TITLE, resizable=False, fullscreen=False)
    # window = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    view = LoseOrWinView("Lose")
    window.show_view(view)

    arcade.run()

if __name__ == "__main__":
    main()

    

