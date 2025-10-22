# 1
def invertText(texto:str):
    """
    Inverte um texto
    Arg: texto - string : o texto que ira ser invertido
    """
    texto=texto[::-1]
    return texto
#2
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
#3
def capicua(texto:str):
    '''
    Verifica se o texto é compicua em caso de verdade retorna True em falso retorna False
    Arg : texto : string : o texto a ser verificado
    '''
    if texto.lower == texto[::-1].lower:
        return True
    else:
        return False
# 5
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
