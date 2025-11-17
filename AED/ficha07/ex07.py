def AddContry(fileName):
    with open(fileName, 'r+' , encoding='utf-8') as file:
        pais = str(input('Idroduza um pais '))
        continente= str(input('Indroduza o continente desse pais '))
        print(file.read())
        lista=(file.read())
        lista=lista.split(',')
        print(lista)
        if lista.count(pais)==0:
            file.write(pais.capitalize()+','+continente.capitalize()+',')
        else:
            print('Esse pais já existe na lista')
    file.close()


pasta = 'files'
fichero = 'países.txt'
with open(fichero, 'a' , encoding='utf-8') as file:
    AddContry(fichero)
    
file.close()
with open(fichero , 'r', encoding='utf-8') as file:    
    print(file.read())
file.close()