"""
#クラスの作成
class Human():
    #コンストラクタの定義
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        
    #メソッドの作成
    def print_data(self):
        print('{}と申します。年は{}で体重は{}kgで身長は{}cmあります。'.format(self.name,self.age,self.weight,self.height))

#継承
class Warumono(Human):
    def __init__(self,name,age,weight,height,line):
        super().__init__(name,age,weight,height)
        self.line = line

    def kaiwa(self):
        print('俺は{}!{}'.format(self.name,self.line))

#インスタンスの作成
human = Human('yamada',30,100,180)
human.print_data()

warumono1 = Warumono('warumono1',100,100,100,'元気ですか？')
warumono1.kaiwa()

#多様性
class Animal():
    def cry(self):
        print('')
        #オーバーライドしてもしなくても良い場合はpass
        #必ずオーバーライドする場合
        raise NotImplementedError
class Cat(Animal):
    def __init__(self,name):
        self.name = name
    #親クラスと同じメソッドを再定義
    def cry(self):
        print(self.name + '「にゃー」')

class Dog(Animal):
    def __init__(self,name):
        self.name = name
    #親クラスと同じメソッドを再定義
    def cry(self):
        print(self.name + '「わん」')

cat = Cat('ミー')
cat.cry()
"""

class Heikin():
    def __init__(self,A):
        self.x,self.y = 0,0
        self.A = A

    def henkan(self):
        self.x = [int(i) for i in self.A]

    def nijyou(self):
        self.x = [i**2 for i in self.x]

    def heikin(self):
        self.y = sum(self.x)/len(self.x)

def kekka(s):
    a = Heikin(s)
    a.henkan()
    a.nijyou()
    a.heikin()
    print(int(a.y))

B = ['1','2','3','4','5']
kekka(B)
