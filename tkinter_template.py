import tkinter
import math
#ボールのデータを設定
ball = {'dirx':15,'diry':-15,'x':300,'y':240,'w':15}

#パドルのデータを設定
paddle = {'paddlewidth':100,'paddleheight':10,'paddlex':260,'paddley':300}

#ブロックのデータを設定
block = {'block_width':50,'block_height':20,'block_x':30,'block_y':20,'block_between':20}

#パドル操作
right_pressed = False
left_pressed = False
paddle_speed = 20

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
    if bx < 0 or bx > 600 :
        ball["dirx"] *= -1
    if by < 0 or by > 400 :
        ball["diry"] *= -1

    #パドルにボールがぶつかったとき
    if paddle['paddlex'] <= bx <= paddle['paddlex']+paddle['paddlewidth'] and paddle['paddley'] == by:
        ball['diry'] *= -1
        
    #移動内容を更新
    if 0 <= bx <= 600: 
        ball["x"] = bx
    if 0 <= by <= 400: 
        ball["y"] = by   

#ブロック描写の関数
def draw_block(a,b,c,d):
    blockrightx = a + c
    blockdowny = b + d
    canvas.create_rectangle(a,b,blockrightx,blockdowny,fill='green')

#パドル描写の関数
def drawpaddle():
    paddlerightx = paddle['paddlex'] + paddle['paddlewidth']
    paddlelefty = paddle['paddley'] + paddle['paddleheight']
    canvas.create_rectangle(paddle['paddlex'],paddle['paddley'],paddlerightx,paddlelefty,fill='green',outline='')

#右矢印を押したとき
def right_key(event):
    global right_pressed
    right_pressed = True

#右矢印を離したとき
def right_key_release(event):
    global right_pressed
    right_pressed = False

#左矢印を押したとき
def left_key(event):
    global left_pressed
    left_pressed = True

#左矢印を離したとき
def left_key_release(event):
    global left_pressed
    left_pressed = False

root.bind('<Right>',right_key)
root.bind('<KeyRelease-Right>',right_key_release)
root.bind('<Left>',left_key)
root.bind('<KeyRelease-Left>',left_key_release)

#ゲームループ
def game_loop():
    draw_objects()
    move_ball()
    drawpaddle()

    #横8縦3のブロックを描写
    j = block['block_y']
    for t in range(3):
        i = block['block_x']
        for d in range(8):
            draw_block(i,j,block['block_width'],block['block_height'])
            i = i + block['block_width'] + block['block_between'] + d - d 
        j = j + block['block_height'] + block['block_between'] + t - t

    root.after(50,game_loop)

    if right_pressed:
        if paddle['paddlex'] + paddle['paddlewidth'] + paddle_speed < 620:
            paddle['paddlex'] += paddle_speed
    
    if left_pressed:
        if paddle['paddlex'] - paddle_speed > -20:
            paddle['paddlex'] -= paddle_speed
            
game_loop()
root.mainloop()