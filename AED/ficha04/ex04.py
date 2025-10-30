#att 1
def dataGrades():
    LisNota=[]
    for x in range(10):
        try:
            nota=float(input(f'A nota do {x+1}º aluno: '))
            if nota<0 and nota>20:
                raise ValueError
            else:
                LisNota.append(nota)
        except ValueError:
            x-=1
            print('nota não valida')
        except:
            x-=1
            print('valor não valido')
            
    media=(sum(LisNota)/10)
    print(media)
    print(f'Nota mais alta: {max(LisNota)}')
    print(f'Nota mais baixa: {min(LisNota)}')
    NMedia=0
    for x in range(10):
        if LisNota[x] >= media:
            NMedia+=1
    print(f'Notas acima da média: {NMedia}')

#att 2
def gamblin():
    from random import randint
    casas=[]
    estrelas=[]
    loop=True
    while loop:
        numero=randint(1,50)
        if casas.count(numero)== 0 and len(casas)<5:
            casas.append(numero)
        else:
            numero=randint(1,12)
        if estrelas.count(numero)==0 and casas.count(numero)== 0 and len(estrelas)<2 and numero<=12:
            estrelas.append(numero)
        if len(casas)==5 and len(estrelas)==2:
            print(f'\n\tCasas {casas}',end='')
            print(f'    Estrelas {estrelas}')
            continuar=str(input('\nrodar novamente s/n: ')).upper()
            casas=[]
            estrelas=[]
            if continuar=='N':
                loop=False

#att 3
def AleatoryList ():
    from random import randint
    Loop=True
    Lista=[]
    NAnt=1
    while Loop:
        Numero=randint(NAnt,100)
        Lista.insert(0,Numero)
        print(f'\tNumero gerado - {Numero} -')
        if Numero == 100:
            Loop=False
            continue
        NAnt=Numero+1
        Continuar=str(input('\nContinuar? s/n: ')).upper()
        if Continuar == 'N' :
            Loop=False
    print(f'\n  -  fim de programa lista final: {Lista}')

#att 4
def Fature():
    Mes=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Desembro']
    Total=[]
    StrTotal=('')
    for Loop in range(12):
        Fatura=float(input(f'\nIndique a fatura do mes de {Mes[Loop]} : '))
        Total.append(Fatura)
    media=(sum(Total)/12)
    print(f'\n\tMedia de faturação {media}')
    print(f'\n\tO melhor mes: {Mes[Total.index(max(Total))]}')
    print(f'\n\tO pior mes: {Mes[Total.index(min(Total))]}')
    NMedia=0

#att 5
def  searchNumber ():
    Lista=[]
    for Loop in range(10):
        Entrada=float(input('\nNumero : '))
        Lista.append(Entrada)
    procura=float(input('\n\tO numero procurado: '))
    if procura in Lista:
        print(f'\nNumero em : ')
        x=0
        while x<10:
           if procura == Lista[x]:
               print(f'{x+1} ',end='')
           x +=1 
    else:
        print('\n - Numero não encontrado - ')

#att 6
def visitens():
    Semana=['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sabado']
    LisVisit=[]
    for Loop in range(7):
        visist=int(input(f'Numero de visitantes na {Semana[Loop]}: '))
        LisVisit.append(visist)
    Loop=0
    while Loop<7: 
        OrdLisVist=sorted(LisVisit,reverse=True)
        numero=LisVisit.index(OrdLisVist[Loop])
        print(Semana[numero], OrdLisVist[Loop])
        Loop+=1
    media=sum(LisVisit)/7
    print('Numero medio de visitantes {:.2f}'.format(media))
    (media - LisVisit[Loop])
visitens()