

# Djangoの学習記録(day3)
## テンプレートとは
htmlなどのWEBページとなるもので、様々な変数などの情報を組み込んだもの  
Djangoはテンプレートを読み込み、変数などに値を代入してページを完成させてからクライアント側に返す  

## 準備
* テンプレートを使うにあたり、作ったtestアプリケーションを登録する必要がある  
Djangoのテンプレート機能が、testアプリケーションを検索できるようにするためである
setting. pyのINSTALLED_APPSにtestアプリケーションを追加し、登録する  
  
* testアプリケーション内に、「templates」というフォルダを作成し、そこにアプリケーション名と同じ名前のフォルダ「test」を作成し、htmlファイルを作成する  
ここでは「index.html」という名前にする

## テンプレート作成  
```html
<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>{{title}}</title>
</head>
<body>
    <h1>{{title}}</h1>
    <p>{{msg}}</p>
</body>
</html>
```
* このhtmlファイルに{{変数名}}という形で変数を埋め込んだ  

そして、views. pyを開き、
```python
def index(request):
    params = {
        'title':'test/index'
        'msg:':'This is sample'
    }
    return render(request, 'test/index.html', params)
```
* テンプレートに渡す値が、paramsに辞書型として登録している
* render関数の引数に、HttpRequestクラスのインスタンスであるrequestと、index.htmlへのパスと、テンプレートに渡す変数を指定している  
  

## 同テンプレートを二つのページで使用する  
index.htmlを編集し、< body >内に以下を追加する
```html
<p><a href="{% url next %}">{{rink}}</a></p>
```
* "{% url ~ %} はurlテンプレートと呼ばれ、~で指定したパスに繋がる(~はurls. pyのpathの名前のこと)
  
views. pyを開き、
```python
def index(request):
    params = {
        'title':'test/index',
        'msg':'This is sample'
        'next':'next',
    }
    return render(request, 'test/index.html', params)

def next(request):
    params = {
        'title':'test/index',
        'msg':'This is next page',
        'next':'index',
    }
    return render(request, 'test/index.html', params)
```
* それぞれの関数が実行されたとき、それぞれのparamsの値が、テンプレートに渡される  


views. pyに新たな関数を作ったので、urls. pyを編集し、
```python
urlpatterns = [
    path('', views.index, name='index'),
    path('next', views.next, name='next'),
]
```
* それぞれのpathに名前を付けることで、{% url 名前 %}でパスと紐づけられる
  
## メモ
次はフォームについて学習する