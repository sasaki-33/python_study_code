# Django学習記録(day10)
## レコードの並び替え
今までレコードは、ID番号が昇順に並べられていた  
他の基準でレコードを並び替える方法として、Managerの「order_by」というメソッドを使用する方法がある  
* Human(モデル名).objects.all.(filter).order_by(項目名) ・・・項目を昇順に並び替える  
* Human.objects.all(filter).order_by(項目名).reverse ・・・項目を降順に並び替える（reverseメソッドを使用する）