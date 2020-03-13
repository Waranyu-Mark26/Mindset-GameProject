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
class TestView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = arcade.load_texture("Resources/game-bg2.jpg")
        #self.Dirt = arcade.Sprite("Resources/HomeButton/home-btn-clicked.png",scale=0.13,center_x=62.5,center_y=658)
        #self.Dirt2 = arcade.Sprite("Resources/HomeButton/home-btn-clicked.png",scale=0.13,center_x=937.5,center_y=658)
        #self.Dirt3 = arcade.Sprite("Resources/HomeButton/home-btn-clicked.png",scale=0.13,center_x=62.5,center_y=162)
        #self.Dirt4 = arcade.Sprite("Resources/HomeButton/home-btn-clicked.png",scale=0.13,center_x=937.5,center_y=162)

    def on_draw(self):
        CreateStageClass = CreateStage()
        CreateStageClass.CheckStage(1)
        IM_STAGE = CreateStageClass.stage_list
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        for i in range(0,len(IM_STAGE)):
            for j in range(0,len(IM_STAGE[i])):
                if IM_STAGE[i][j] == 1:
                    #print(62.5+(j*125),720-((i+1)*62))
                    self.Dirt = arcade.Sprite("Resources/HomeButton/home-btn-locked.png",scale=0.13,center_x=62.5+(j*125),center_y=658-(i*124))
                elif IM_STAGE[i][j] == 2:
                    self.Dirt = arcade.Sprite("Resources/HomeButton/home-btn-hover.png",scale=0.13,center_x=62.5+(j*125),center_y=658-(i*124))
                if IM_STAGE[i][j] != 0:
                    self.Dirt.draw()
    
        super().on_draw()

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False, fullscreen=False)
    menu_view = TestView()
    window.show_view(menu_view)
      
    arcade.run()

if __name__ == "__main__":
    main()


'''ลองรันดูนะจ๊ะ
ยืมรูปก่อนเน้อ'''