# externos
import matplotlib.pyplot as plt
import csv


fileName='./AED/ficha08/carros_usados.csv'
listaCarro=['']
quantia=[]

with open(fileName,newline='', encoding='utf-8') as file:
    lista=csv.DictReader(file, delimiter = ',')
    listaAA=list(lista)
    marca=('')
    quant=0
    for linha in listaAA:
        if marca != linha['Make']:
            listaCarro.append(linha['Make'])
            quantia.append(quant)
            marca=linha['Make']
            quant=0
        else:
            quant+=1
    quantia.append(quant)
 
    # controlo
    print(quantia)
    print(listaCarro)
    
    # ^fonte
    font1={'family':'serif','color':'blue','size':18}
    
    # grafico de onda
    plt.title('Marca de carro',fontdict=font1,loc='center')
    plt.xlabel('Marca')
    plt.ylabel('Variedades de carro')
    eixoY=(quantia[1],quantia[2],quantia[3],quantia[4],quantia[5],quantia[6],quantia[7])
    eixoX=('audi','BMW','Ford','Vw','toyota','skoda','Hyundai')
    plt.plot(eixoX,eixoY,
             linestyle='dotted',
             marker='D',
             ms=5,
             mfc='red')
    plt.show()
    
    # grafico de pizza
    myexplode=[0.2,0.2,0.2,0.2,0.2,0.2,0.2]
    plt.title('Marca de carro',fontdict=font1,loc='center')
    plt.pie(eixoY,
        labels=eixoX,
        autopct='%1.1f%%',
        explode=myexplode,shadow=True
    )
    plt.show()