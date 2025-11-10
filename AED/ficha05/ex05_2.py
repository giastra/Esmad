def showData(rainfall):
    '''
    uma tabela 2d com a 1ª linha sendo as cidades e nas outras linhas tem que possuir os meses na 1ª casa 
    '''
    for w in range(len(rainfall[0])):
        print('    ',rainfall[0][w],'\t',end='')
        for e in range(len(rainfall)-1):
            print(rainfall[e+1][w+1],'\t',end='')
        print('')

rainfall=[['Braga','Porto','Lisboa'],['Janeiro'],['Fevereiro'],['Março'],['Abril'],['Maio'],['Junho']]

for x in range(3):
    print('Pulveresidade em ',rainfall[0][x])
    for n in range(len(rainfall)-1):
        numero=int(input(f'{rainfall[n+1][0]} :'))
        rainfall[n+1].append(numero)

print('\ttabela de pulveresidade')
showData(rainfall)
coluna=[]
linha=[]
for l in range(3):
    for x in range(len(rainfall)-1):
        soma=0
        soma+=rainfall[x+1][l+1]
        coluna.append(soma)
         
for x in range(len(rainfall)-1):
    for l in range(3):
        z=0
        z+=rainfall[x+1][l+1]
        linha.append(z)


print('\nbraga: {:.1f} , porto: {:.1f} , Lisboa: {:.1f}'.format((sum(coluna[0:5])/6),(sum(coluna[6:11])/6),(sum(coluna[12:17])/6)))

print('\njaneiro: {:.1f}, fevereiro {:.1f} , março: {:.1f} , Abril: {:.1f} , maio: {:.1f} , junho: {:.1f}'.format((sum(linha[0:3])/3),(sum(linha[3:6])/3),(sum(linha[6:9])/3),(sum(linha[9:12])/3),(sum(linha[12:15])/3),(sum(linha[15:18])/3)))
