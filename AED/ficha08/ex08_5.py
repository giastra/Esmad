import matplotlib.pyplot as plt
import csv
fileName='./AED/ficha08/carros_usados.csv'

with open(fileName,newline='', encoding='utf-8') as file:
    lista=csv.DictReader(file, delimiter = ',')
    listaAA=list(lista)
print('Marcas: audi, BMW, Ford, Vw, toyota, skoda, Hyundai')
marca=input('Qual marca que deseja visualizar as vendas:')
dinP=0
dinD=0
dinH=0
for linha in listaAA:
    if linha['Make']==marca:
        dinheiro=int(linha['price'])
        if linha['fuelType'] == 'Petrol':
            dinP+=dinheiro
            
        elif linha['fuelType'] == 'Diesel':
            dinD+=dinheiro

        elif linha['fuelType'] == 'Hybrid':
            dinH+=dinheiro
print('Disel',dinD,' Hidrido',dinH,' petrolho',dinP)
font1={'family':'serif','color':'blue','size':12}
plt.title(f'Quantidade vendida por tipo de combustivel da {marca}',fontdict=font1,loc='center')
plt.xlabel('Tipo de combustivel')
plt.ylabel('Quantidade de venda')
eixoX=('Petrol','Disel','Hybrid')
eixoY=(dinP,dinD,dinH)
plt.bar(eixoX,eixoY,color='red')
plt.show()