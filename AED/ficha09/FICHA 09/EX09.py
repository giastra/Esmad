import csv
import numpy as np
import matplotlib.pyplot as plt
import os



filePath = './AED/ficha09/FICHA 09/files/'
fileName = filePath+ "films.csv"



def loadDataFilms():
    """
    Retorna os dados dos filmes e o header (nomes dos atributos)
    """
    with open(fileName,newline='', encoding='utf-8') as file:
        lista=csv.reader(file, delimiter = ',')
        header=next(lista)
        filmsData=list(lista)

    return filmsData,header



def showDatasetResume():
    """
    Mostra um resumo do dataset
    """
    
    print('Number films : ',np.shape(filmsData)[0])
    print('\nDimension of films data : ',np.shape(filmsData)[0],' films')
    print('\nAtributes of dataset: ',np.shape(filmsData)[1], 'atributes')
    print('\nAtributes names:')
    for atribures in header: 
        print(' - ',atribures)



def cleanDataset(filmsData):
    """
    Limita o dataset a 100 filmes e remove filmes com rating ou género vazio
    Retorna o dataset limpo
    """
    filmsData=filmsData[1:100]
    indexRating=header.index('rating')
    indexGenere=header.index('genre')
    removeFilms=[]
    for film in filmsData:
        if film[indexRating]==''or film[indexGenere]=='':
            removeFilms.append(film)

    for film in removeFilms:
        filmsData.remove(film)
        
    print('\nNumber of films after cleaning: ',len(filmsData))
    return filmsData                                                                                                   



def showFilmsByGenre():
    """
    calcula e mostra Nº e filmes por género através de:
    - Gráfico de barras 
    - Gráfico circular (pie chart)
    """
    genereItems=[]
    genereCount=[]
    indexGenere=header.index('genre')
    for film in filmsData:
        genres=film[indexGenere].split(', ')
        for genre in genres:
            if genre in genereItems:
                pos = genereItems.index(genre)
                genereCount[pos]+=1
            else:
                genereItems.append(genre)
                genereCount.append(1)


    plt.figure(figsize=(12,6)) 
    
    # primeiro grafico de barra
    plt.subplot(1,2,1) 
    plt.bar(genereItems,genereCount)
    plt.xlabel('Genre')
    plt.ylabel('Number of Films')
    plt.title('Number of Films by Genre')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    #  segundo grafico de pizza
    plt.subplot(1,2,2)
    myexplode=[]
    for x in range(len(genereItems)):
        myexplode.append(0.2)
    plt.pie(genereCount,
            labels=genereItems,
            autopct='%1.1f%%',
            explode=myexplode)
    plt.show()
def showFilmsByRating():
    """
    Mostra uma análise dos filmes por rating: 
    -Nº filmes com rating >= 8.0 
    - Nº filmes com rating entre 7.0 e 7.9
    - Nº filmes com rating < 7.0
    """



def showTopRating(top):
    """
    Determinar e mostrar os top filmes por rating
    """
    


#----------------------------------------------------------------
# Main Program
os.system('cls')
filmsData, header = loadDataFilms()
showDatasetResume()
filmsData = cleanDataset(filmsData)
 
showFilmsByGenre()
showFilmsByRating()

top=10
showTopRating(top)