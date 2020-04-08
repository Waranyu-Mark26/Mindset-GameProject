import arcade
from arcade.gui import *
import globalvars as var

WIDTH = var.SCREEN_WIDTH
HEIGHT = var.SCREEN_HEIGHT

# Game Button
space_y = 60
space_X = 60
start_x = 1050
start_y = 670
max_x_panel = 1220

class GameView(arcade.View):
    def __init__(self,previous_window, level):
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

        self.setup(level)
        self.previous_window = previous_window

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
            self.Character = arcade.Sprite("Resources/Animations/Right.png",scale=0.20,center_x=62.5,center_y=306) #y +20 จากตรงกลาง
            self.c_x,self.c_y = 0,3
            self.dir_cha = "Right"
        elif level == 2:
            self.Character = arcade.Sprite("Resources/Animations/Right.png",scale=0.20,center_x=62.5,center_y=554)
            self.c_x,self.c_y = 0,1
            self.dir_cha = "Right"
        elif level == 3:
            self.Character = arcade.Sprite("Resources/Animations/Front.png",scale=0.20,center_x=62.5,center_y=678)
            self.c_x,self.c_y = 0,0
            self.dir_cha = "Down"
        self.list_Character.append(self.Character)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            self.menu = self.previous_window
            self.window.show_view(self.menu)

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
        
        if self.Start:
            if self.lenLi >= len(self.List): self.Start = False

            #GoAhead
            elif self.List[self.lenLi] == 1:
                if self.dir_cha == 'Down':
                    self.Character.change_y = -6 #ตอนรูปนิ่ง animation อาจเปลี่ยนแปลงนะจ๊ะ
                    if self.Character.center_y <= 678 - ((self.c_y+1)*124):
                        self.Character.change_y = 0
                        self.c_y += 1
                        self.lenLi += 1
                elif self.dir_cha == 'Up':
                    self.Character.change_y = 6
                    if self.Character.center_y >= 678 - ((self.c_y-1)*124):
                        self.Character.change_y = 0
                        self.c_y -= 1
                        self.lenLi += 1
                elif self.dir_cha == 'Right':
                    self.Character.change_x = +5
                    if self.Character.center_x >= 62.5 + ((self.c_x+1)*125): 
                        self.Character.change_x = 0
                        self.c_x += 1
                        self.lenLi += 1
                elif self.dir_cha == 'Left':
                    self.c_x -= 1
                    self.Character.change_x = -5
                    if self.Character.center_x <= 62.5 + ((self.c_x-1)*125):
                        self.Character.change_x = 0
                        self.c_x -= 1
                        self.lenLi += 1
                
            #TurnLeft
            elif self.List[self.lenLi] == 2:
                self.Character.remove_from_sprite_lists()
                if self.dir_cha == 'Down':
                    self.dirsprite = "Resources/Animations/Right.png"
                    self.dir_cha = 'Right'
                elif self.dir_cha == 'Up':
                    self.dirsprite = "Resources/Animations/Left.png"
                    self.dir_cha = 'Left'
                elif self.dir_cha == 'Right':
                    self.dirsprite = "Resources/Animations/Front.png"
                    self.dir_cha = 'Up'
                elif self.dir_cha == 'Left':
                    self.dirsprite = "Resources/Animations/Front.png"
                    self.dir_cha = 'Down'
                self.Character = arcade.Sprite(self.dirsprite,scale=0.20,center_x=62.5+(self.c_x*125),center_y=678-(self.c_y*124))
                self.list_Character.append(self.Character)
                self.lenLi += 1

            # TurnRight
            elif self.List[self.lenLi] == 3:
                self.Character.remove_from_sprite_lists()
                if self.dir_cha == 'Down':
                    self.dirsprite = "Resources/Animations/Left.png"
                    self.dir_cha = 'Left'
                elif self.dir_cha == 'Up':
                    self.dirsprite = "Resources/Animations/Right.png"
                    self.dir_cha = 'Right'
                elif self.dir_cha == 'Right':
                    self.dirsprite = "Resources/Animations/Front.png"
                    self.dir_cha = 'Down'
                elif self.dir_cha == 'Left':
                    self.dirsprite = "Resources/Animations/Front.png"
                    self.dir_cha = 'Up'
                self.Character = arcade.Sprite(self.dirsprite,scale=0.20,center_x=62.5+(self.c_x*125),center_y=678-(self.c_y*124))
                self.list_Character.append(self.Character)
                self.lenLi += 1
            
            #checkBlock
            #if self.IM_STAGE[self.c_y][self.c_x] != 1 and self.IM_STAGE[self.c_y][self.c_x] != 2:

                    
            #elif self.IM_STAGE[self.c_y][self.c_x] == 2:

            

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
        self.game.list_output = arcade.SpriteList()
        self.game.List.clear()
        self.game.Move_x = start_x
        self.game.Move_y = start_y

        self.pressed = True

    def on_release(self):
        if self.pressed:
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
'''
def main():
    window = arcade.Window(WIDTH, HEIGHT, SCREEN_TITLE, resizable=False, fullscreen=False)

    game = GameView(3)
    window.show_view(game)

    arcade.run()

if __name__ == "__main__":
    main()
    '''