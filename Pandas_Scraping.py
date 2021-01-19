#pandasモジュールの宣言
import pandas as pd 

#tableタグを持つサイトのURLを変数に入れる
url = 'サイトのURL'
#データフレームとしてデータの取得
dfs = pd.read_html(url)

#textデータとして表示
for i in dfs:
    with open('sample.txt','a',encoding = 'utf_8') as file:
        file.write('{}'.format(i))