#at 1
def invertText(texto:str):
    """
    Inverte um texto
    Arg: texto - string : o texto que ira ser invertido
    """
    texto=texto[::-1]
    return texto
#at 2
def contText (texto:str,tipo=1):
    '''
    Conta a quantidade de letras, espaços e vogais
    Arg: texto - string : o texto para ser quantificado
    Arg: tipo - string : qual o modo que quer , 1-caracteres , 2-vogais, 3-espaços
    ex= conText(x,1) irá interpretar o x e contar a quantidade de caracteres
    em caso de falha irá retornar : nd
    '''
    if tipo==1:
        texto=len(texto)
        return texto
    elif tipo ==2:
       numero=(texto.lower()).count('a')
       numero+=(texto.lower()).count('e')
       numero+=(texto.lower()).count('i')
       numero+=(texto.lower()).count('o')
       numero+=(texto.lower()).count('u')
       return numero
    elif tipo == 3:
       texto=texto.count(' ')
       return texto
    else:
        return ('nd')
#at 3
def capicua(texto:str):
    '''
    Verifica se o texto é compicua em caso de verdade retorna True em falso retorna False
    Arg : texto : string : o texto a ser verificado
    '''
    if texto.lower == texto[::-1].lower:
        return True
    else:
        return False
#at 4
def removeSpaces(texto:str):
    texto=texto.split(' ')
    tamanho=len(texto)
    cont=0
    mfinal=''
    while cont < tamanho:
        if texto[cont] == '':
            cont +=1 
        else:
            mfinal+=f' {texto[cont]}'
            cont +=1 
    return mfinal.strip()
#at 5
def shortName(texto:str):
    texto=texto.split(' ')
    reduzido=f'{texto[0]} {texto[len(texto)-1]}'
    return reduzido
#at 6
def standardName(texto:str):
    texto=texto.split(' ')
    lopin=1
    retorno=texto[0]
    while lopin < len(texto)-1:
        algo=texto[lopin]
        retorno=retorno+f' {algo[0]}.'
        lopin+=1
    retorno = retorno +f' {texto[len(texto)-1]}'
    return retorno
#at 7
def generatePassword(userName):
    '''
    não adimite espaços, caso tenha um retorna -1
    '''
    from random import randint
    tamanho=len(userName)
    senha=''
    contador=0
    if userName.find(' ') != -1:
        return -1
    else:
        while contador < tamanho:
            if contador%2==0:
                senha+=userName[randint(0,tamanho-1)]
            else:
                senha+=str(randint(1,9))
            contador+=1
        return senha
#at 8
def reverseWords(texto:str):
    texto=texto.split(' ')
    tamanho=len(texto)
    contador=0
    textoF='' 
    while contador < tamanho:
        local=tamanho-contador
        textoF+=f'{texto[local-1]} '
        contador+=1
    return textoF.strip()
#at 9
def CharLine(texto:str,numberChar:int):
    tamanho=len(texto)
    textoF=''
    contador=0
    caracteres=0
    while contador<tamanho:
        if caracteres < numberChar:
            textoF+=texto[contador]
            caracteres+=1
            contador+=1
        else:
            textoF+='\n'
            caracteres=0
    return textoF

#parte para testar as atividades
print('\n  - Bem vindo a central de atividades da ficha 03')
print('\n\t1-Espelha um texto\n\t2-Conta a quantidade de letras/vogais/espaços da frase\n\t3-Verifica se o texto é capocua\n\t4-Remove espaços extras de uma frase\n\t5-Faz uma versão reduzida de um nome\n\t6-Faz uma versão abraviada de um nome\n\t7-Cria uma senha custumisada para um nickname\n\t8-inverte um texto\n\t9-Alinha um texto de acordo com a quantidade de caracteres por linha')
att=int(input('\n : Itroduza o numero da atividade que deseja testar : '))
if att == 1:
    texto=str(input('\nIntroduza o texto para ser espelhado: '))
    print(f'\n - {invertText(texto)}')
elif att == 2:
    tipo=int(input('\n\t1-Todas\n\t2-Vogais\n\t3-Espaços\n : Introduza o tipo de caractere que deseja contar : '))
    texto=str(input('\n : Introduza o texto a ser conatado : '))
    if tipo == 1:
        coisa='caracteres'
    elif tipo == 2:      
        coisa='vogais'  
    elif tipo == 3:
        coisa='espaços'
    else:
        print('\n\t~ Escolha não valida ~')
    print(f'\n\tExistem {contText(texto,tipo)} {coisa} no seu texto')
elif att == 3:
    texto=str(input('\n : Introduza o texto a ser analisado : '))
    if capicua(texto) == True:
        print('\tO texto é capicua')
    else:
        print('\tO texto não é capicua')
elif att == 4:
    texto=str(input('\n : Introduza o texto a ser tratado : '))
    print(removeSpaces(texto))
elif att == 5:
    texto=str(input('\n : Introduza o nome para ser encurtado : '))
    print(shortName(texto))
elif att == 6:
    texto=str(input('\n : Introduza o nome para ser abreviada : '))
    print(standardName(texto))
elif att == 7:
    texto=str(input('\n : Introduza o username para gerar uma senha : '))
    print(generatePassword(texto))
elif att == 8:
    texto=str(input('\n : Introduza o texto a ser invertido : '))
    print(reverseWords(texto))
elif att == 9:
    texto=str(input('\n : Introduza o texto a ser formatado : '))
    ln=int(input('\t : Introduza a quantidade de caracteres que cada linha vai ter : '))
    print(CharLine(texto,ln))
else:
    print('\n\t~ Atividade não valida ~')