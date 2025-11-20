def AddContry(fileName):
    with open(fileName, 'r+' , encoding='utf-8') as file:
        pais = str(input('Introduza um país '))
        continente= str(input('Introduza o continente desse país '))
        lista=file.read()
        lista=lista.split(',')
        print(lista)
        if lista.count(pais)==0:
            file.write(pais.capitalize()+','+continente.capitalize()+',')
        else:
            print('Esse pais já existe na lista')
    file.close()

def showCountries(fileName):
    with open(fileName , 'r', encoding='utf-8') as file:    
        lista=file.read()
        lista=lista.split(',')
    n=0
    for x in range(len(lista)-1):
        if x%2==0:
            print('\n\t',lista[x],end=' ')
        else:
            print(lista[x])
        
pasta = 'files'
fichero = 'países.txt'
    
while True:
    print('MENU\n1-\n2-\n3-\n4-\n0-')
    intro = int(input('\topção: '))
    if intro == 1:
        AddContry(fichero)
    elif intro == 2:
        showCountries(fichero)
    elif intro == 0:
        break
    else:
        print('\nOpção não valida, tente novamente')   