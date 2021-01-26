#文字型の数式を用意、空白不可
example = '123+45'
#文字型の数式の数字、演算子、括弧をそれぞれリストに格納
expression = [i for i in example]

#数字が複数桁の時、結合し一つの文字として扱う
def henkan(ex):
    basic = 0
    #リストの最後を示す文字を追加
    ex.append('%')
    moji = 0
    #スタックの機能を果たすリストを用意
    stack = []
    while moji < len(ex):
        #文字が数字、もしくは最後の要素か
        if '0' <= ex[moji] <= '9' or ex[moji] == '%':
            stack.append(ex[moji])
        #文字が演算子か    
        if ex[moji] == '*' or ex[moji] == '/' or ex[moji] == '+' or ex[moji] == '-' or ex[moji] == '(' or ex[moji] == ')':
            stack.append(ex[moji])

        #スタックの最後の要素が、演算子またはexpressionの最後の要素ならば、それ以前の文字を結合
        if stack[-1] == '*' or stack[-1] == '/' or stack[-1] == '+' or stack[-1] == '-' or stack[-1] == '(' or stack[-1] == ')' or stack[-1] == '%' :
            r,total = 0,0
            while r < len(stack)-1:
                #結合する文字は数字なのでint型にして結合
                total = total + int(stack[r])*(10**(len(stack)-r-2))
                r += 1
            #文字型に直す
            total = str(total)
            ex[basic] = total
            #結合することで余分となったexpressionの要素を削除
            while moji > basic + 1:
                moji -= 1
                ex.remove(ex[moji])
            #演算子以降の文字の結合のためにスタックを空に戻す        
            stack.clear()
            basic = moji + 1
        moji += 1
    #exの最後を示す要素を削除
    expression.remove(ex[-1])
    return ex

def kaiseki(ext):
    #int型の数値を保持するリストを用意
    value = []
    value.append(0)
    #演算子を保持するリストを用意
    operator = []
    #演算を行う優先順位を保持するリストを用意
    priority = []
    op,nest,i = 0,0,0

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
    
