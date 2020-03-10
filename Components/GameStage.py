import arcade
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
SCREEN_TITLE = 'Test Adventure'
class StageCreate:

    def CheckStage(self,stage=1):
        if stage == 1:
            self.stage_list = [[0,0,0,0,0,0,0,0],[0,0,1,1,1,1,0,0],[0,0,1,0,0,1,1,2,],[1,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        else:
            self.stage_list = []

    def GoStage(self):
        self.CheckStage()
        for i in range(0,len(self.stage_list)):
            self.ShowStage(i=i)

    def ShowStage(self,i):
        print(self.stage_list[i])

#Test
class TestView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = arcade.load_texture("Resources/View 1.jpg")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        super().on_draw()

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False, fullscreen=False)
    # window = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    menu_view = TestView()
    window.show_view(menu_view)
      
    arcade.run()

if __name__ == "__main__":
    main()


test = StageCreate()
test.GoStage()