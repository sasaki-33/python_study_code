import tkinter

#ボールのデータを設定
ball = {'dirx':20,'diry':-20,'x':300,'y':240,'w':15}

#ウィンドウの作成
root = tkinter.Tk()
root.title('sample_game')
root.minsize(600,400)
#画面の作成
canvas = tkinter.Canvas(width = 600,height = 400)
canvas.pack()

def draw_objects():
    #既存の画面を削除
    canvas.delete('all')
    #円型のボールを作成
    canvas.create_oval(ball["x"] - ball["w"], ball["y"] - ball["w"],ball["x"] + ball["w"], ball["y"] + ball["w"],fill = 'green')

def move_ball():
    #移動後の数値を代入
    bx = ball["x"] + ball["dirx"]
    by = ball["y"] + ball["diry"]
    #xy画面を超えたとき
    if bx < 0 or bx > 600: 
        ball["dirx"] *= -1
    if by < 0 or by > 400: 
        ball["diry"] *= -1
    #移動内容を更新
    if 0 <= bx <= 600: 
        ball["x"] = bx
    if 0 <= by <= 400: 
        ball["y"] = by   
#ゲームループ
def game_loop():
    draw_objects()
    move_ball()
    root.after(50,game_loop)

game_loop()
root.mainloop()