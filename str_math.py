#文字型の数式を用意、空白不可
example = '24+45'
#文字型の数式の数字、演算子、括弧をそれぞれリストに格納
expression = [i for i in example]

#数字が複数桁の時、結合し一つの文字として扱う
basic = 0
#リストの最後を示す文字を追加
expression.append('%')
moji = 0
#スタックの機能を果たすリストを用意
stack = []
while moji < len(expression):
    #文字が数字、もしくは最後の要素か
    if '0' <= expression[moji] <= '9' or expression[moji] == '%':
        stack.append(expression[moji])
    #文字が演算子か    
    if expression[moji] == '*' or expression[moji] == '/' or expression[moji] == '+' or expression[moji] == '-' or expression[moji] == '(' or expression[moji] == ')':
        stack.append(expression[moji])

    #スタックの最後の要素が、演算子またはexpressionの最後の要素ならば、それ以前の文字を結合
    if stack[-1] == '*' or stack[-1] == '/' or stack[-1] == '+' or stack[-1] == '-' or stack[-1] == '(' or stack[-1] == ')' or stack[-1] == '%' :
        t = 0
        while t < len(stack)-2:
            total = stack[t] + stack[t+1]
            t += 1
        expression[basic] = total
        #結合することで余分となったexpressionの要素を削除
        while moji > basic + 1:
            expression.remove(expression[moji-1])
            moji -= 1
        #演算子以降の文字の結合のためにスタックを空に戻す        
        stack.clear()
        basic = moji + 1
    moji += 1

expression.remove(expression[-1])
print(expression)
"""
#int型の数値を保持するリストを用意
value = []
value.append(0)
#演算子を保持するリストを用意
operator = []
#演算を行う優先順位を保持するリストを用意
priority = []

op,nest,i = 0,0,0
while i < len(expression):
    chr = expression[i]
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
"""
