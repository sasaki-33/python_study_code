#mathをインポート
import math

#シンプソン積分を求め、10^9し、小数点を切り捨てる関数の定義
def simpson(a):
    i = 0
    kekka = 0
    h = 1/(2*a)
    
    #被積分関数の計算を行う関数の定義
    def kansuu(b):
        c = 0
        if b == 0:
            c = 1
        else:
            c = math.sqrt(1-((b*h)**2))
        return c
    
    while i < a :
        kekka = kekka + kansuu(2*i) + 4*kansuu(2*i+1) + kansuu(2*i+2)
        i += 1
    
    final_a = (kekka*h)/3
    final_b = math.floor(final_a*(10**9))
    return final_b

#分割数の初期値を設定
Nx = 2
Ny = Nx + 2

#NxとNyの値が一致するまで分割数を増やす
while simpson(Nx) != simpson(Ny) :
    Nx = Ny
    Ny = Ny + 2

#10^9で割り、元の積分値に戻す
rule = simpson(Nx)/(10**9)

#結果の表示
print('一致した分割数は{}である。'.format(Nx))
print('題意を満たす積分値は{}である。'.format(rule))