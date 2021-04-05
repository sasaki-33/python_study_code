# 検索について
## フィルターについて
モデルのobjects属性のManagerに、「フィルター」という検索に関係する機能がある  
フィルターを使い、テーブルに保存したレコードの中から条件に合致するレコードを検索することができる  

## フィルターを使用する
モデル名.objects.filter(フィルターの内容)で使用できる  
フィルターを使用するにあたり、viewsに関数を新規作成する  
まずは、urls. pyを編集し、  
```python
path('find', views.find, name = 'find'),
```  
このパスを追加し、test/findにアクセスした時に、find関数を実行するようにする  
次に、フィルターの内容を書き込むフォームを作成する  
forms. pyに以下のクラスを追加する  
```python
class FindForm(forms.Form):
    find = forms.CharField(label = 'find', required = False)
```  
* HumandFormクラスのように、forms.Formを継承し、Formクラスを作成する  

find関数を作成する
```python
# 作ったFindFormをインポート
from .forms import FindForm
# 略
def find(request):
    # POST送信されたとき
    if (request.method == 'POST'):
        # フォームのインスタンスを作成
        form = FindForm(request.POST)

        # POST送信された'find'の値を変数に格納する
        find = request.POST['find']
        # フィルターで名前を指定し、レコードを変数に格納する
        data = Human.objects.filter(name = find) # レコードの項目名 = 値

        # POST送信された時のメッセージ内容
        msg = 'result is :' + str(data.count())
    else:
        msg = 'data is ...'
        # 空フォームを表示
        form = FindForm()
        # POST送信でない場合、全てのレコードを表示
        data = Human.objects.all()
    
    params = {
        'title':'search',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request, 'test/find.html', params)
```  

検索用のテンプレートを新規作成する  
```html
<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>{{title}}</title>
</head>
<body>
    <h1>{{title}}</h1>
    <p>{{message|safe}}</p>
    <form action="{% url 'find' %}" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <tr><th></th><td>
        <input type="submit" value="click"></td></tr>
    </form>
    <hr>
    <table>
        <tr>
            <th>id</th>
            <th>name</th>
            <th>mail</th>
        </tr>
    {% for item in data %}
        <tr>
            <td>{{item.id}}</td>
            <td>{{item.name}}</td>
            <td>{{item.mail}}</td>
    {% endfor %}
    </table>
</body>
</html>
```  
これで、検索が可能になる  
検索で使用するfilterは、繋げて複数の条件を使用することができる  
ANDの場合、(例) Human.objects.filter(項目名 = 値).filter(項目名 = 値)  
ORの場合、以下を追記し、
```python
from django.db.models import Q
```  
(例) Human.objects.filter(Q(項目名 = 値) | Q(項目名 = 値))

## 様々な検索条件の方法
### あいまい検索
filterメソッドでは「項目名＝値」で検索を行っていたが、このままでは完全にその値と一致するレコードしか検索できない  
そこで、値が含まれている場合にそれを取り出せるあいまい検索を行う  
* Human.objects.filter(項目名__contains = 値) ・・・　値を含む検索
* Human.objects.filter(項目名__strtswith = 値)・・・　値で始まるものの検索  
* Human.objects.filter(項目名__endswith = 値)・・・　値で終わるものの検索  

### 大文字と小文字の区別
filter検索では、大文字と小文字を区別する  
大文字と小文字を区別しない場合は、以下を使用する
* Human.objects.filter(項目名__iexact = 値)  
また、大文字と小文字を区別せず、かつあいまい検索を行いたい場合は以下を使う  
* Human.objects.filter(項目名__icontains = 値)  
* Human.objects.filter(項目名__istartswith = 値)  
* Human.objects.filter(項目名__iendswith = 値)  

### 数値検索の範囲
数値で検索する場合、大小関係を指定できる  
* Human.objects.filter(項目名__gt = 数値)・・・　数値より大きいものを検索
* Human.objects.filter(項目名__gte = 数値)・・・　数値以上のものを検索
* Human.objects.filter(項目名__lt = 値)・・・　数値より小さいものを検索
* Human.objects.filter(項目名__lte = 値)・・・　値より大きいものを検索  

### リストで検索
リストを用意し、中の値と一致するレコードを全て取り出すことが出来る  
```python
# フォームで送信された値を取り出す
find = request.POST['find']
# 値をリストに変換
list = find.split()
# リストに含まれる値を検索する
data = Human.objects.filter(項目名__in = list)
```  
* フォームには、半角スペースで値を書き出せばよい
