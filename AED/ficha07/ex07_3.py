import matplotlib.pyplot as plt
import csv
fileName='./AED/ficha07/carros_usados.csv'
marca=input('Qual marca que deseja analisar: ')
listaCarro=[]
with open(fileName,newline='', encoding='utf-8') as file:
    lista=csv.DictReader(file, delimiter = ',')
    listaAA=list(lista)
    for linha in listaAA:
        if marca == linha['Make']:
            listaCarro.append(int(linha['price']))
clac=(sum(listaCarro)/len(listaCarro))
print('{:.2f}'.format(clac))
