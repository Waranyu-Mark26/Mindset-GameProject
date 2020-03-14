import arcade
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
SCREEN_TITLE = 'Test Adventure'
class CreateStage():
    
    def __init__(self,stage_list = []):
        self.stage_list = stage_list

    def CheckStage(self,stage=1):
        if stage == 1:
            self.stage_list = [[0,0,0,0,0,0,0,0],[0,0,1,1,1,1,0,0],[0,0,1,0,0,1,1,2],[1,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        if stage == 2:
            self.stage_list = [[0,0,0,0,0,0,0,0],[1,1,1,3,1,1,1,2],[0,1,0,0,1,0,0,0],[0,1,1,1,1,0,0,0],[0,0,0,0,0,0,0,0]]
        #return CreateStage(self.stage_list)
    
'''เทสเฉยๆ
    def GoStage(self):
        STAGE_CODE = self.CheckStage()
        for i in range(0,len(STAGE_CODE)):
            self.ShowStage(i,STAGE_CODE)

    def ShowStage(self,i,ST):
        print(ST[i])
        '''

#Test
class GameStageView(arcade.View):
    def __init__(self,x):
        super().__init__()
        self.block_list = None
        self.flag_list = None
        self.background = arcade.load_texture("Resources/game-bg2.jpg")
        CreateStageClass = CreateStage()
        CreateStageClass.CheckStage(x)
        IM_STAGE = CreateStageClass.stage_list
        self.block_list = arcade.SpriteList()
        self.setup(IM_STAGE)

    def setup(self,ST):
        self.block_list = arcade.SpriteList()
        for y in range(0,len(ST)):
            for x in range(0,len(ST[y])):
                if ST[y][x] == 1:
                    #print(62.5+(x*125),720-((y+1)*62))
                    Dirt = arcade.Sprite(":resources:images/tiles/stone.png",scale=0.65,center_x=62.5+(x*125),center_y=658-(y*124))
                    self.block_list.append(Dirt)
                elif ST[y][x] == 2:
                    Dirt = arcade.Sprite(":resources:images/tiles/stone.png",scale=0.65,center_x=62.5+(x*125),center_y=658-(y*124))
                    self.block_list.append(Dirt)
                    Flag = arcade.Sprite(":resources:images/items/flagYellow1.png",scale=0.65,center_x=62.5+(x*125)+35,center_y=658-(y*124)+60)
                    self.block_list.append(Flag)
                elif ST[y][x] == 3:
                    Lava = arcade.Sprite(":resources:images/tiles/lava.png",scale=0.65,center_x=62.5+(x*125),center_y=658-(y*124))
                    self.block_list.append(Lava)
                


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.block_list.draw()    
    
        super().on_draw()

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False, fullscreen=False)
    menu_view = GameStageView(1)
    window.show_view(menu_view)
      
    arcade.run()

if __name__ == "__main__":
    main()


'''ลองรันดูนะจ๊ะ
ยืมรูปก่อนเน้อ'''