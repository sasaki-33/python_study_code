from PIL import Image

#image.jpgの読み込み
img = Image.open('image.jpg')

#(x,y)=(450,780)から(650,980)の部分を切り取り
cropped_img = img.crop((450,780,650,980))

#切り取った部分を新たな画像として保存
#cropped_img.save('img2.jpg')

#image.jpgの読み込み
img2 = Image.open('image2.jpg')

#(100,100)のRGB値の取得
iro = img2.getpixel((100,100))
print(iro)
#(1,1)のRGB値の取得
iro2 = img2.getpixel((1,1))
print(iro2)