# Django学習記録(day6)
## データベースについて
Djangoが対応しているデータベースはMySQL、PostgreSQL、SQLiteの三つがある  
これらは、SQLというデータアクセス言語を用いて、データベースを操作する  
データベースには二種類のタイプが存在し、  
1. サーバタイプ・・・データベースにアクセスするためのサーバプログラムを起動し、WEBサーバとデータベースサーバ間で通信を行う(MySQL,PostgreSQL)  
2. エンジンタイプ・・・データベースのファイルに直接アクセスするエンジンプログラム(SQLite)  
* pythonには標準でSQLiteが組み込まれている  
django_appプロジェクト内のdjango_appフォルダの「setting. py」で設定を行い、デフォルトでSQLiteの設定をしている  

データベースは保存するデータ構造を定義する「テーブル」と、保存するデータの「レコード」からなる  
Djangoではデータベースのテーブルを直接作ることはせず、データベースのスクリプトにより自動的にデータベースにテーブルを作成してくれる  

## テーブルの定義
Djangoでは、モデルクラスの作成が、データベースのテーブルの定義となる  
そして、そのモデルクラスのインスタンスが、実際のレコードとなる

## モデルクラスの作成
アプリケーションフォルダ内の「models. py」を編集し、
```python
from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    mail = models.EmailField(max_length=50)
    gender = models.BooleanField()
    birthday = models.DateField()

    def __str__(self):
        return '<name=' + str(self.name) +'(' + str(self.age) + ')>'
```
* django.db.modelsのModelクラスを継承し、モデルクラスを作成する
* 変数=フィールドのインスタンスの形式で保管する値に関する変数を用意する
* 「__ str __」を用意することにより、テキストとして表示する内容を編集することが可能になる

## マイグレーションを行う
マイグレーションとはデータベースの移行を担う機能  
また、プロジェクトでデータベースをアップデートするのにも使い、空のデータベースに、モデルを元にテーブルを作成することも可能にする  

マイグレーションは、「マイグレーションファイルの作成」、「マイグレーションの適用」の手順で行う  
ターミナルで、「python manage. py makemigration アプリケーションの名前」でマイグレーションファイルを作成する  
また、「python manage. py migrate」でマイグレーションの適用を行う  

