import arcade
from arcade.gui import *
import time

WIDTH = 1280
HEIGHT = 720

# Game Button
space_y = 60
space_X = 60
start_x = 1050
start_y = 670
max_x_panel = 1220

class LoseOrWinView(arcade.View):
    def __init__(self,loseorwin,level = 1,menu=None,stage=None):
        super().__init__()
        self.loseorwin = loseorwin
        self.other = Theme()
        self.mainmenu = Theme()
        self.stage = Theme()
        self.other.set_font(30,arcade.color.WHITE,font_name=('Arial'))
        self.newlevel = level
        self.set_buttons()
        self.mainmenu = menu #รับหน้า menu
        self.stage = stage #รับหน้า stage
        arcade.set_background_color(arcade.color.AMAZON)

        #setBackground
        if self.loseorwin == "Lose":
            self.background = arcade.load_texture("Resources/game-bg4.jpg")
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
            self.button_list.append(Button(x=640,y=430,text='NEXT LEVEL',theme= self.other,view= self.newlevel,game=self))
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
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            
            if self.view != None:
                if self.view == 0:
                    print('KUY')
                    menu = self.game.mainmenu
                elif 1 <= self.view <= 4:
                    if self.text == 'TRY AGAIN':
                        menu = GameView(self.game.stage,self.view,self.game.mainmenu)
                    elif self.text == 'NEXT LEVEL':
                        menu = GameView(self.game.stage,self.view+1,self.game.mainmenu)
                elif self.view == 5:
                    if self.text == 'TRY AGAIN':
                        menu = GameView(self.game.stage,self.view,self.game.mainmenu)
                    elif self.text == 'NEXT LEVEL':
                        menu = self.game.stage
                self.game.window.show_view(menu)

class GameView(arcade.View):
    def __init__(self,previous_window, level,menu):
        super().__init__()
        arcade.set_background_color(arcade.color.AMAZON)
        self.background = arcade.load_texture("Resources/game-bg2.jpg")
        # If you have sprite lists, you should create them here,
        # and set them to None

        # Flow Stage
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

        # Game Control
        self.Play = Theme()
        self.Stop = Theme()

        #Play Control
        self.Start = False
        self.lenLi = 0

        # Game Stage
        self.block_list = None
        self.flag_list = None
        self.background = arcade.load_texture("Resources/game-bg2.jpg")
        CreateStageClass = CreateStage()
        CreateStageClass.CheckStage(level)
        self.IM_STAGE = CreateStageClass.stage_list
        self.block_list = arcade.SpriteList()
        
        self.level = level
        self.menu_view = menu
        self.setup(level)
        self.previous_window = previous_window

        self.iterator = 0
        self.start_move = True
    

    def set_button_texturesPlay(self):
        normal = "Resources/PlayButton/play-btn-normal.png"
        hover = "Resources/PlayButton/play-btn-hover.png"
        clicked = "Resources/PlayButton/play-btn-clicked.png"
        locked = "Resources/PlayButton/play-btn-locked.png"
        self.Play.add_button_textures(normal, hover, clicked, locked)

    def set_button_texturesStop(self):
        normal = "Resources/StopButton/stop-btn-normal.png"
        hover = "Resources/StopButton/stop-btn-hover.png"
        clicked = "Resources/StopButton/stop-btn-clicked.png"
        locked = "Resources/StopButton/stop-btn-locked.png"
        self.Stop.add_button_textures(normal, hover, clicked, locked)

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

        self.set_button_texturesPlay()
        self.set_button_texturesStop()

    def set_buttons(self):
        # Game Command
        self.button_list.append(forwardButton(self,350,60,100,100,theme=self.forward))
        self.button_list.append(turnleftButton(self,500,60,100,100,theme=self.turnleft))
        self.button_list.append(turnrightButton(self,650,60,100,100,theme=self.turnright))

        # Game Control
        self.button_list.append(PlayButton(self, 1100, 80, 130, 130,theme=self.Play))
        self.button_list.append(StopButton(self, 1210, 60, 80, 80,theme=self.Stop))     

    def setup(self,level):
        # Create your sprites and sprite lists here
        self.setup_theme()
        self.set_buttons()

        self.block_list = arcade.SpriteList()
        self.list_Character = arcade.SpriteList()
        for y in range(0,len(self.IM_STAGE)):
            for x in range(0,len(self.IM_STAGE[y])):
                if self.IM_STAGE[y][x] == 1:
                    #print(62.5+(x*125),720-((y+1)*62))
                    Dirt = arcade.Sprite(":resources:images/tiles/stone.png",scale=0.65,center_x=62.5+(x*125),center_y=658-(y*124))
                    self.block_list.append(Dirt)
                elif self.IM_STAGE[y][x] == 2:
                    Dirt = arcade.Sprite(":resources:images/tiles/stone.png",scale=0.65,center_x=62.5+(x*125),center_y=658-(y*124))
                    self.block_list.append(Dirt)
                    Flag = arcade.Sprite(":resources:images/items/flagYellow1.png",scale=0.65,center_x=62.5+(x*125)+35,center_y=658-(y*124)+60)
                    self.block_list.append(Flag)
                elif self.IM_STAGE[y][x] == 3:
                    Lava = arcade.Sprite(":resources:images/tiles/lava.png",scale=0.65,center_x=62.5+(x*125),center_y=658-(y*124))
                    self.block_list.append(Lava)
        if level == 1:
            self.dirCharacter = "Resources/Character/character-right.png"
            self.c_x,self.c_y = 0,3
            self.dir_cha = "Right"
        elif level == 2:
            self.dirCharacter = "Resources/Character/character-right.png"
            self.c_x,self.c_y = 0,1
            self.dir_cha = "Right"
        elif level == 3:
            self.dirCharacter = "Resources/Character/character-down.png"
            self.c_x,self.c_y = 0,0
            self.dir_cha = "Down"
        elif level == 4:
            self.dirCharacter = "Resources/Character/character-up.png"
            self.c_x,self.c_y = 3,4
            self.dir_cha = "Up"
        elif level == 5:
            self.dirCharacter = "Resources/Character/character-right.png"
            self.c_x,self.c_y = 0,2
            self.dir_cha = "Right"
        self.Character = arcade.Sprite(self.dirCharacter,scale=0.40,center_x=62.5+(self.c_x*125),center_y=678-(self.c_y*124))
        self.list_Character.append(self.Character)

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
        height = 120
        #arcade.draw_lrtb_rectangle_outline(start_x, start_x + width,
                                           #start_y + height, start_y,
                                           #arcade.color.WHITE, 1)
        
        start_y = 120
        start_x = 0
        width = 1000
        height = 600
        #arcade.draw_lrtb_rectangle_outline(start_x, start_x + width,
                                           #start_y + height, start_y,
                                           #arcade.color.WHITE, 1)
        
        start_y = 0
        start_x = 1000
        width = 280
        height = 200
        #arcade.draw_lrtb_rectangle_outline(start_x, start_x + width,
                                           #start_y + height, start_y,
                                           #arcade.color.WHITE, 1)

        # Draw Game Stage
        self.block_list.draw()
        self.list_Character.draw()

        super().on_draw()
        # Call draw() on all your sprite lists below

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            self.menu = self.previous_window
            self.window.show_view(self.menu)

    

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if self.PressUp and len(self.List) < 32:
            Button = arcade.Sprite("Resources/Arrow/Arrow-up-normal.png",scale=0.25,center_x=self.Move_x,center_y=self.Move_y)
            self.list_output.append(Button)
            self.List.append(1)
            if self.Move_x >= max_x_panel:
                self.Move_y -= space_y
                self.Move_x = start_x
            else:
                self.Move_x += space_X
            self.PressUp = False

        if self.PressLeft and len(self.List) < 32:
            Button = arcade.Sprite("Resources/Arrow/Arrow-turn left-normal.png",scale=0.25,center_x=self.Move_x,center_y=self.Move_y)
            self.list_output.append(Button)
            self.List.append(2)
            if self.Move_x >= max_x_panel:
                self.Move_y -= space_y
                self.Move_x = start_x
            else:
                self.Move_x += space_X
            self.PressLeft = False

        if self.PressRight and len(self.List) < 32:
            Button = arcade.Sprite("Resources/Arrow/Arrow-turn right-normal.png",scale=0.25,center_x=self.Move_x,center_y=self.Move_y)
            self.list_output.append(Button)
            self.List.append(3)
            if self.Move_x >= max_x_panel:
                self.Move_y -= space_y
                self.Move_x = start_x
            else:
                self.Move_x += space_X
            self.PressRight = False

        # Game Section
        if self.Start:
            if self.lenLi >= len(self.List): 
                #checkWin
                if self.IM_STAGE[self.c_y][self.c_x] == 2 and self.lenLi >= (len(self.List)-1):
                    self.menu = LoseOrWinView("Win",level= self.level,menu =self.menu_view,stage =self.previous_window)
                    self.window.show_view(self.menu)
                self.Start = False

            #GoAhead
            elif self.List[self.lenLi] == 1:
                if self.start_move:
                    time.sleep(0.5)
                    self.list_output[self.lenLi].alpha = 150
                    self.start_move = False

                if self.dir_cha == 'Down':
                    self.Character.change_y = -8 #ตอนรูปนิ่ง animation อาจเปลี่ยนแปลงนะจ๊ะ
                    if self.Character.center_y <= 678 - ((self.c_y+1)*124):
                        self.Character.change_y = 0
                        self.c_y += 1
                        self.lenLi += 1

                        self.start_move = True
                elif self.dir_cha == 'Up':
                    self.Character.change_y = 8
                    if self.Character.center_y >= 678 - ((self.c_y-1)*124):
                        self.Character.change_y = 0
                        self.c_y -= 1
                        self.lenLi += 1

                        self.start_move = True
                elif self.dir_cha == 'Right':
                    self.Character.change_x = 8
                    if self.Character.center_x >= 62.5 + ((self.c_x+1)*125): 
                        self.Character.change_x = 0
                        self.c_x += 1
                        self.lenLi += 1

                        self.start_move = True
                elif self.dir_cha == 'Left':
                    self.Character.change_x = -8
                    if self.Character.center_x <= 62.5 + ((self.c_x-1)*125):
                        self.Character.change_x = 0
                        self.c_x -= 1
                        self.lenLi += 1

                        self.start_move = True
            #TurnLeft
            elif self.List[self.lenLi] == 2:
                self.Character.remove_from_sprite_lists()
                if self.dir_cha == 'Down':
                    self.dirsprite = "Resources/Character/character-right.png"
                    self.dir_cha = 'Right'
                elif self.dir_cha == 'Up':
                    self.dirsprite = "Resources/Character/character-left.png"
                    self.dir_cha = 'Left'
                elif self.dir_cha == 'Right':
                    self.dirsprite = "Resources/Character/character-up.png"
                    self.dir_cha = 'Up'
                elif self.dir_cha == 'Left':
                    self.dirsprite = "Resources/Character/character-down.png"
                    self.dir_cha = 'Down'
                self.list_output[self.lenLi].alpha = 150
                self.Character = arcade.Sprite(self.dirsprite,scale=0.40,center_x=62.5+(self.c_x*125),center_y=678-(self.c_y*124))
                self.list_Character.append(self.Character)
                self.lenLi += 1
                time.sleep(0.25)

            # TurnRight
            elif self.List[self.lenLi] == 3:
                self.Character.remove_from_sprite_lists()
                if self.dir_cha == 'Down':
                    self.dirsprite = "Resources/Character/character-left.png"
                    self.dir_cha = 'Left'
                elif self.dir_cha == 'Up':
                    self.dirsprite = "Resources/Character/character-right.png"
                    self.dir_cha = 'Right'
                elif self.dir_cha == 'Right':
                    self.dirsprite = "Resources/Character/character-down.png"
                    self.dir_cha = 'Down'
                elif self.dir_cha == 'Left':
                    self.dirsprite = "Resources/Character/character-up.png"
                    self.dir_cha = 'Up'
                self.list_output[self.lenLi].alpha = 150
                self.Character = arcade.Sprite(self.dirsprite,scale=0.40,center_x=62.5+(self.c_x*125),center_y=678-(self.c_y*124))
                self.list_Character.append(self.Character)
                self.lenLi += 1
                time.sleep(0.25)

            #checkLose
            if self.c_y >= len(self.IM_STAGE) or self.c_y < 0 or self.c_x >= len(self.IM_STAGE[0]) or self.c_x < 0 :
                self.menu = LoseOrWinView("Lose",level= self.level,menu = self.menu_view,stage = self.previous_window)
                self.window.show_view(self.menu)

            elif self.IM_STAGE[self.c_y][self.c_x] != 1 and self.IM_STAGE[self.c_y][self.c_x] != 2:
                self.menu = LoseOrWinView("Lose",level= self.level,menu = self.menu_view,stage = self.previous_window)
                self.window.show_view(self.menu)

              

        self.list_output.update()
        self.list_Character.update()


class CreateStage():
    def __init__(self,stage_list = []):
        self.stage_list = stage_list

    def CheckStage(self,stage=1):
        if stage == 1:
            self.stage_list = [[0,0,0,0,0,0,0,0],[0,0,1,1,1,1,0,0],[0,0,1,0,0,1,1,2],[1,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        elif stage == 2:
            self.stage_list = [[0,0,0,0,0,0,0,0],[1,1,1,3,1,1,1,2],[0,1,0,0,1,0,0,0],[0,1,1,1,1,0,0,0],[0,0,0,0,0,0,0,0]]
        elif stage == 3:
            self.stage_list = [[1,0,1,1,1,0,0,0],[1,0,1,0,1,0,1,2],[1,0,1,0,1,0,1,0],[1,0,1,0,1,0,1,0],[1,1,1,0,1,1,1,0]]
        elif stage == 4:
            self.stage_list = [[0,1,1,1,1,0,0,0],[1,2,0,0,1,1,1,1],[3,0,0,0,3,0,0,1],[1,1,1,1,1,1,1,1],[0,0,0,1,0,0,0,0]]
        elif stage == 5:
            self.stage_list = [[0,1,1,3,1,1,1,1],[0,1,0,0,1,0,0,1],[1,1,1,3,1,3,1,2],[0,1,0,0,1,0,0,3],[0,1,1,1,1,1,1,1]]

class PlayButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.Start = True
            self.pressed = False

class StopButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        #self.game.list_output = arcade.SpriteList()
        #self.game.List.clear()
        #self.game.Move_x = start_x
        #self.game.Move_y = start_y

        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.list_output = arcade.SpriteList()
            self.game.List.clear()
            self.game.Move_x = start_x
            self.game.Move_y = start_y
            self.game.lenLi = 0
            self.game.Character.change_y = 0
            self.game.Character.change_x = 0
            self.game.Character.remove_from_sprite_lists
            game = GameView(self.game.previous_window,self.game.level,self.game.menu_view)
            self.game.window.show_view(game)
            self.pressed = False

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

SCREEN_TITLE = "Algorithm Adventure"

def main():
    window = arcade.Window(WIDTH, HEIGHT, SCREEN_TITLE, resizable=False, fullscreen=False)

    game = GameView(GameView, 1, GameView)
    window.show_view(game)

    arcade.run()

if __name__ == "__main__":
    main()
