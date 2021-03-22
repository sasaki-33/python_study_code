

# Django学習記録(day4)
## フォームとは
フォームはユーザとのやり取りを行う基本的な機能  
特に重要なのが、「テキストの入力フィールドで値を送信する」ということ  

## Formクラス
FormクラスはDjangoに備わっているフォームのクラスであり、このクラスを使用し、フォームの内容をPythonクラスとして定義する  
そしてテンプレートに変数として渡すことで、クラスの内容からフォームが自動的に作られる  

## Formクラスを使用する
「test」フォルダ内に「forms. py」という名前のファイルを作成する
```python
from djago import forms


class TestForm(forms.Form):
    name = forms.CharField(label = 'name')
    mail = forms.CharField(label = 'mail')
    age = forms.InterField(label = 'age')
```
* forms.Formというクラスを継承し、TestFormというクラスを定義する
* forms.CharFieldはテキストを入力する一般的なフィールドのクラス
* forms.InterFieldは整数の値を入力するためのフィールドクラス
* forms.(CharField or InterField)の引数にlabelというラベル名を設定することで、インスタンスをそれぞれの変数に格納している

「views. py」を編集し、
```python
from .forms import TestForm

def index(request):
    params = {
        'title':'Test',
        'msg':'your data',
        'form':TestForm()
    }
    if (request.method == 'POST'):
        params['msg'] = 'name:' + request.POST['name'] + \
            '<br>mail:' + request.POST['mail'] + \
            '<br>age:' + request.POSt['age']
        params['form'] = TestForm(request.POST)

    return render(request, 'test/index.html', params)
```
* index関数の前半の部分が共通でテンプレートに渡す値
* if文以降はPOST時の処理
* if文でPOST送信されたかどうかの判断をしている
* POST送信された場合は、paramsのキーが'msg'と'form'である値を更新している
* 共通処理の部分で'form'キーにTestFormクラスを置き、更新時に送られてきたフォームの値でインスタンスを作成している  

「index.html」を編集し、
```html
{% load static %}
<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>{{title}}</title>
    <link rel="stylesheet" href="bootstrapのURL" crossorigin="anonymous">
    </head>
<body class="container">
    <h1 class="display-4 text-primary">{{title}}</h1>
    <p class="h5 mt-4">{{message|safe}}</p>
    <form action="{% url 'index' %}" method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="click">
    </form>
</body>
</html>
```
* index関数のparamsで用意した'form'にはTestFormクラスのインスタンスが設定されているので、views. py実行時にはTestFormクラスによりフォームが自動生成される  