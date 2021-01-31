"""
文字型で与えられた計算式を、数字、演算子、括弧に分けリストに格納し、
それぞれの要素を演算の優先順位を考慮しながら演算を行い結果を返すプログラムである。
数字には桁が存在しないので、複数桁の数値が存在する時、一度数値に変換し一つの文字としてリストに格納する必要がある。
演算処理ではリストの要素から数字、演算子に分けそれぞれの演算の順序を決めるリストも作成する。
"""

#数字が複数桁の時、結合し一つの文字として扱う
def henkan(ex):
    basic = 0
    #リストの最後を示す文字を追加
    ex.append('%')
    moji = 0
    #スタックの機能を果たすリストを用意
    stack = []
    while moji < len(ex):
        #文字が数字、演算子、もしくは最後の要素か
        if '0' <= ex[moji] <= '9' or ex[moji] == '%' or ex[moji] == '*' or ex[moji] == '/' or ex[moji] == '+' or ex[moji] == '-' or ex[moji] == ')' :
            stack.append(ex[moji])

        #stackに二文字しかない場合は結合する必要が無いのでstackの内容を削除
        if len(stack) == 2 and (stack[-1] == '*' or stack[-1] == '/' or stack[-1] == '+' or stack[-1] == '/' or stack[-1] == ')' or stack[-1] == '%'):
            stack.clear()

        #stackの中身が演算子または%しかない場合は次の要素を参照するためにstackを削除しておく
        if len(stack) == 1 and (stack[0] == '*' or stack[0] == '/' or stack[0] == '+' or stack[0] == '-' or stack[0] == '%'):
            stack.clear()

        #スタックの最後の要素が、演算子またはexpressionの最後の要素ならば、それ以前の文字を結合
        if len(stack) > 0 and (stack[-1] == '*' or stack[-1] == '/' or stack[-1] == '+' or stack[-1] == '-' or stack[-1] == ')' or stack[-1] == '%' ):
            r,total = 0,0
            while r < len(stack)-1:
                #結合する文字は数字なのでint型にして結合
                total = total + int(stack[r])*(10**(len(stack)-r-2))
                r += 1
            #文字型に直す
            total = str(total)
            #結合の基準点にtotalの内容を移す
            ex[basic] = total
            #結合することで余分となったexpressionの要素を削除
            while moji > basic + 1:
                moji -= 1
                ex.remove(ex[moji])

            #演算子以降の文字の結合のためにスタックを空に戻す        
            stack.clear()

            #結合の基準点を前括弧の最初の要素に移す
            if ex[moji] != '%' and ex[moji+1] == '(':
                basic = moji + 2
            else:
                basic = moji + 1

        #moji=0の時、ex[moji]が前括弧であれば基準のbasicを1増やす
        if moji == 0 and ex[moji] == '(':
            basic += 1
        
        #結合した後に括弧がくるならば、あらかじめ参照する要素番号をスキップする
        if ex[moji] != '%' and len(stack) == 0 and (ex[moji+1] == '(' or ex[moji+1] == '%'):
            moji += 2
        else:
            moji += 1

    #exの最後を示す要素を削除
    ex.remove(ex[-1])
    return ex

#文字型の数式を用意、空白不可
example = '45*(20-12)'
#文字型の数式の数字、演算子、括弧をそれぞれリストに格納
expression = [i for i in example]


#解析処理と計算処理を行う関数
def kaiseki(ext):
    #int型の数値を保持するリストを用意
    value = []
    value.append(0)
    #演算子を保持するリストを用意
    operator = []
    #演算を行う優先順位を保持するリストを用意
    priority = []
    op,nest,i = 0,0,0

    #解析処理
    while i < len(ext):
        chr = ext[i]
        if '0' <= chr <= '9':
            value[op] = 10*value[op] + int(chr)
    
        if chr == '+' or chr == '-' or chr == '*' or chr == '/':
            operator.append(chr)
            if chr == '+' or chr == '-':
                priority.append(nest + 10)
            else:
                priority.append(nest + 20)

            op += 1
            value.append(0)
    
        if chr == '(':
            nest += 30
    
        if chr == ')':
            nest -= 30

        i += 1  

    #計算処理
    while op > 0:
        it = 0
        i = 1
        #priority配列の優先順位を比べ数値の大きい方をitに設定
        while i < op:
            if priority[it] < priority[i]:
                it = i
            i += 1

        chr = operator[it]
        #演算を行う
        if chr == '+':
            value[it] = value[it] + value[it+1]
        if chr == '-':
            value[it] = value[it] - value[it+1]
        if chr == '*':
            value[it] = value[it] * value[it+1]
        if chr == '/':
            value[it] = value[it] / value[it+1]
        
        i = it + 1

        while i < op:
            value[i] = value[i+1]
            operator[i-1] = operator[i]
            priority[i-1] = priority[i]
            i += 1
        
        op -= 1
    #value[0]に入れた演算結果を返す
    return value[0]