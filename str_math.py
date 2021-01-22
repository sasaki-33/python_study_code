#文字型の数式を用意
example = '2*(9-(8+4)/2)'
#文字型の数式の数字、演算子、括弧をそれぞれリストに格納
expression = [i for i in example]


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
