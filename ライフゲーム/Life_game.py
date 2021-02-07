import tkinter
from random import randint

#セルが存在するステージの行と列
cols,rows = 30,20
#セルのサイズ
size = 20
#ステージの情報をリストで保持
data = []
#ステージの情報をランダムに設定
for j in range(0,rows):
    #リスト内包表記を利用し、1列にcolsの数だけ行を作成する
    data.append([(randint(0,9) == 0) for i in range(0,cols)])

#ウィンドウの作成
win = tkinter.Tk()
#キャンバスの作成
cv = tkinter.Canvas(win,width = 600,height = 400)
cv.pack()

#セルの条件の定義
def dead_or_alive(x,y):
    #周囲の生存セルを数える
    count = 0
    #テーブルの情報をリストとして保持
    tabel = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
    for i in tabel:
        x2,y2 = x + i[0],y + i[1]
        if 0 <= x2 < cols and 0 <= y2 < rows:
            if data[y2][x2]:
                count += 1

    #誕生の条件に合致するとき
    if count == 3:
        return True
    #生存の条件に合致するとき
    if data[y][x]:
        if 2 <= count <= 3:
            return True
        #過疎or過密のとき
        else:
            return False
    
    return data[y][x]

#データを次世代に更新する関数
def sedai():
    global data
    new_data = []
    for y in range(0,rows):
        new_data.append([dead_or_alive(x, y) for x in range(0,cols)])
    #dataに次世代の情報を更新する
    data = new_data

#ステージの描画
def draw_stage():
    #キャンバスの内容を破棄
    cv.delete('all')
    for y in range(0, rows):
        for x in range(0, cols):
            if not data[y][x]:
                continue
            
            #x1,y1の値を更新
            x1,y1 = [x*size, y*size]
            #楕円を描く
            cv.create_oval(x1,y1,x1+size,y1+size,fill="green",width=0)