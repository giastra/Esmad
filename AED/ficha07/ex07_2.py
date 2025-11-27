def writeText(text):
     file = open(fileName, 'wb')
     file.write(text.encode('utf-32'))
     file.close()

def readText():
     file=open(fileName,'rb')
     texto=file.read().decode('utf-32')
     print(texto)

# def  readText():
fileName='./AED/ficha07/text.bin'
text=input('o texto a ser introduzido: ')
writeText(text)

readText()