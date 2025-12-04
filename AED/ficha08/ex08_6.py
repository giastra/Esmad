import matplotlib.pyplot as plt
import csv
fileName='./AED/ficha08/carros_usados.csv'

with open(fileName,newline='', encoding='utf-8') as file:
    lista=csv.DictReader(file, delimiter = ',')
    listaAA=list(lista)
dinP=0
dinD=0
dinH=0
for linha in listaAA:
        if linha['fuelType'] == 'Petrol':
            dinP+=1
            
        elif linha['fuelType'] == 'Diesel':
            dinD+=1

        elif linha['fuelType'] == 'Hybrid':
            dinH+=1
print('Disel',dinD,' Hidrido',dinH,' petrolho',dinP)
eixoX=('Petrol','Disel','Hybrid')
eixoY=(dinP,dinD,dinH)
font1={'family':'serif','color':'blue','size':18}
plt.title('Vendas por tipo de combustivel',fontdict=font1,loc='center')
plt.pie(eixoY,
        labels=eixoX,
        autopct='%1.1f%%',
        shadow=True
    )
plt.show()