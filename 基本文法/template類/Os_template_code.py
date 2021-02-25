import os

#現在のディレクトリパスの表示
print(os.getcwd())

#現在のディレクトリに存在するファイル名やフォルダ名をリストで返す
print(os.listdir())

#指定したパスに存在するファイル名やフォルダ名をリストで返す
print(os.listdir('build'))

#一つ上のディレクトリに移動
os.chdir('..')
#相対パスを指定してディレクトリを移動
os.chdir('./Python Scripts')

#指定した要素がファイルかどうか判定する
print(os.path.isfile('./chromedriver.exe'))

#ファイルの拡張子を切り離し、タプル型で返す
print(os.path.splitext('./chromedirver.exe'))

#ディレクトリの作成
os.mkdir('./aiueo')
#名前の変更
os.rename('aiueo','kakikukeko')
#指定したディレクトリが存在するかどうか判定する
print(os.path.exists('kakikukeko'))
#ディレクトリの削除
os.remove('kakikukeko')