
def showTable(n):
    from random import randint
    tabela=[[],[],[]]
    for l in range(n):
        for x in range(n):
            num=randint(0,9)
            tabela[l].append(num)
    return tabela
def verifyTable(tabela,n):
    '''
    tabela com 2d 
    0 para coluna 
    1 para linha
    '''
    coluna=[]
    linha=[]
    for l in range(3):
        soma=0
        for x in range(3):
            soma+=tabela[x][l] 
        coluna.append(soma)
        linha.append(sum(tabela[l]))
    if n == 0:
        return coluna
    if n == 1:
        return linha

print('lista aleatoria')
tabela=showTable(3)
for l in range(len(tabela)):
    print('\t',end='')
    for x in range(len(tabela)):
        print(tabela[l][x],end=' ')
    print('\n')
print('soma dos resultados das linhas: ',verifyTable(tabela,1))
print('soma dos resultadso das colunas: ',verifyTable(tabela,0))
