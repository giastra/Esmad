from PIL import Image

pathImages = './images/'

newSize = (250,250)
imagem = Image.new(size=newSize, mode='RGB',color='white')

pixelMap = imagem.load()
for i in range(imagem.width):
    for j in range(imagem.height):
        red = i
        green=j
        blue=255-i
        pixelMap[i,j]=(red,green,blue)
imagem.show()
imagem.save('pathImages'+'teste1.jpg')