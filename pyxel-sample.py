#pyxelモジュールの宣言
import pyxel

#クラスの作成
class App():
    #属性の定義
    def __init__(self):
        pyxel.init(180,220,scale=3)
        self.x = 80
        self.y = 100
        #updateメソッドとdrawメソッドを実行
        pyxel.run(self.update,self.draw)

    #updateメソッドの定義  
    def update(self):
        pyxel.load('pyxresのファイル')
        #qを押した時終了
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.draw_c()
        
    def draw_c(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = min(self.x+3,pyxel.width-16)
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = max(self.x-3,0)
        if pyxel.btn(pyxel.KEY_UP):
            self.y = max(self.y-3,0)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y = min(self.y+3,pyxel.height-16)
        if pyxel.btn(pyxel.KEY_LEFT) and pyxel.btn(pyxel.KEY_UP):
            self.x = max(self.x-1,0)
            self.y = max(self.y-1,0)
        if pyxel.btn(pyxel.KEY_RIGHT) and pyxel.btn(pyxel.KEY_UP):
            self.x = min(self.x+1,pyxel.width-16)
            self.y = max(self.y-1,0)
        if pyxel.btn(pyxel.KEY_LEFT) and pyxel.btn(pyxel.KEY_DOWN):
            self.x = max(self.x-1,0)
            self.y = min(self.y+1,pyxel.height-16)   
        if pyxel.btn(pyxel.KEY_RIGHT) and pyxel.btn(pyxel.KEY_DOWN):
            self.x = min(self.x+1,pyxel.width-16)
            self.y = min(self.y+1,pyxel.height-16)
    #drawメソッドの定義        
    def draw(self):
        pyxel.cls(1)
        pyxel.blt(self.x,self.y,0,0,0,16,16)

#クラスの実行        
App()