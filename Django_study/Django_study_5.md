# Django学習記録(day5)
## ビュー関数のクラス化
「views. py」のビュー関数をクラス化することで、処理を単純化できる

## viewクラスの作成
```python
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import TestForm


class TestView(TemplateView):
    def __init__(self):
        self.params = {
            'title':'Test'
            'msg':'your data'
            'form':TestForm()
        }
    
    def get(self, request):
        return render(request, 'test/index.html', self.params)

    def post(self, request):
        msg = 'you are, <b>' + request.POST['name'] + \
            'and' + request.POST['age'] + 'years old' + \
                '</b>' + '<br>mail is ' + request.POST['mail'] + '</br>'
        self.params['msg'] = msg
        self.params['form'] = TestForm(request.POST)
        return render(request, 'test/index.html', self.params)
```
* TemlateViewクラスを継承し、クラスを定義する  
templateViewクラスはビューを扱うViewクラスの派生クラス
* クラス内にGETを扱うメソッド、POSTを扱うメソッドを作成する
  
「urls. py」を編集し、
```python
from django.conf.urls import url
from .views import TestView

ulspatterns = [
    url(r'', TestView.as_view(), name = 'index')
]
```
* 今までは「view. py」内の関数を作るたびにパスとの紐づけが必要だったが、クラスを作ることで「urls. py」のパスを一つ定義するだけで済む  

## フィールドクラス
1. CharField... 文字入力のためのクラスで、インスタンスの作成時に入力に関する設定を行える  
   * required... 必須項目にするかどうかを示すもので、Trueに設定すれば必須項目になる
   * min(max)_length... 最小文字数、最大文字数を指定でき、整数値で指定する

2. EmailField... メールアドレスの入力のためのクラス  
メールアドレスの形式のみ入力可能  
required,min_length,maxlengthを引数に指定可能

3. IntegerField... 整数値の入力のためのクラス
   * min(max)_value... 最小値、最大値を指定するもの

4. FloatField... 実数値の入力のためのクラス  
required,max_value,max_valueを引数に指定可能

5. URLField... URLの入力のためのクラス、存在するかではなく形式のチェックを行う  
required,max_length,max_lengthを引数に指定可能

6. DateField... 日時の形式の入力のためのクラス(2021-03-24,03/24/2021,03/24/21)

7. TimeField... 時刻の形式の入力のためのクラス(11:05,11:05:30)

8. DateTimeField... 日付と時刻を続けて入力するためのクラス