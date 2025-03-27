#f = open('text.txt', 'r', encoding='utf-8')
#text = f.read()
#print(text)
#f.close()



#f= open("text.txt", "a", encoding="utf-8")
#text= "Bu bir deneme metnidir."
#f.write(text)
import os
from PIL import Image

with open("resimler/1.jpg", "rb") as f:
    resim = Image.open(f)
    resim.show()

print(os.listdir('resimler'))