import matplotlib.pyplot as plt
import csv
fileName='./AED/ficha08/carros_usados.csv'

with open(fileName,newline='', encoding='utf-8') as file:
    lista=csv.DictReader(file, delimiter = ',')
    listaAA=list(lista)
print('Marcas: audi, BMW, Ford, Vw, toyota, skoda, Hyundai')
marca=input('Qual marca que deseja visualizar as vendas por tipo de carro:')
eixoX=[]
eixoY=[]
for linha in listaAA:
    if linha['Make']==marca:
        try:
            if eixoX.index(linha['model']) >0:
                eixoY[eixoX.index(linha['model'])]+=1

        except ValueError:
            eixoX.append(linha['model'])
            eixoY.append(1)

print(eixoX,'  ',len(eixoX))
print(eixoY,'  ',len(eixoY))

font1={'family':'serif','color':'blue','size':18}
font2={'family':'serif','size':8}
plt.title('Quantidade de carro/tipo de combustivel',fontdict=font1,loc='center')
plt.xlabel('Tipo de combustivel')
plt.ylabel('Variedades de carro')
plt.plot(eixoX,eixoY,
         marker='o',
        ms=5,
            )
plt.show()