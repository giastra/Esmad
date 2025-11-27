# externos
import matplotlib.pyplot as plt
import csv


fileName='./AED/ficha08/carros_usados.csv'

with open(fileName,newline='', encoding='utf-8') as file:
    lista=csv.DictReader(file, delimiter = ',')
    listaAA=list(lista)
    quant=0
    dinP=[]
    dinD=[]
    dinH=[]
    dinheiro=0
    
    for linha in listaAA:
        dinheiro=float(linha['price'])
        if linha['fuelType'] == 'Petrol':
            dinP.append(dinheiro)
        
        elif linha['fuelType'] == 'Diesel':
            dinD.append(dinheiro)

        elif linha['fuelType'] == 'Hybrid':
            dinH.append(dinheiro)


    mediaP=sum(dinP)/len(dinP)
    mediaD=sum(dinD)/len(dinD)
    mediaH=sum(dinH)/len(dinH)

    print('Petrol. Media:{:.1f}, Min: {:.1f}, Max:{:.1f}'.format(mediaP,min(dinP),max(dinP)))
    print('Disel. Media:{:.1f}, Min: {:.1f}, Max:{:.1f}'.format(mediaD,min(dinD),max(dinD)))
    print('Hybrid. Media:{:.1f}, Min: {:.1f}, Max:{:.1f}'.format(mediaH,min(dinH),max(dinH)))
    
    font1={'family':'serif','color':'blue','size':18}
    plt.title('Quantidade de carro/tipo de combustivel',fontdict=font1,loc='center')
    plt.xlabel('Tipo de combustivel')
    plt.ylabel('Variedades de carro')
    eixoX=('Petrol','Disel','Hybrid')
    eixoY=(mediaP,mediaD,mediaH)
    plt.plot(eixoX,eixoY,
            marker='o',
            ms=5,
            mfc='red')
    MinY=(min(dinP),min(dinD),min(dinH))
    plt.plot(eixoX,MinY,
            marker='d',
            ms=5,
            mfc='white')
    MaxY=(max(dinP),max(dinP),max(dinP))
    plt.plot(eixoX,MaxY,
            marker='p',
            ms=5,
            mfc='blue')
    legenda=('Media','Minimo','Maximo')
    plt.legend(legenda,loc='upper rigth')
    plt.show()

