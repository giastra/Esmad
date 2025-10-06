 
print('Uma central de todas as atividades do exercicio 1\n\n1-Conversor de temperatura ºC -> Fº\n2-Um pequeno teste de cadastro\n3-Calculo de peso ideal')
nAtividade = int(input('\nIndique qual atividade que deseja visualizar: '))

if nAtividade == 1:
    #um conversor de (t)emperatura
    tCelsius=float(input('A temperatura em Cº: '))
    tFahrenheit=(1.8*tCelsius+32)
    print('\nA temperatura em Fº {:.2f}'.format(tFahrenheit))

elif nAtividade == 2:
    #um programa que solicite ao utilizador para indicar o seu nome próprio  (primeiro nome) 
    # e o seu apelido (sobrenome), e apresente o resultado no formato Apelido, Nome 
    Nome=input('Nome proprio: ')
    Apelido=input('\nApelido: ')
    print ('\n %s, %s'%(Apelido,Nome))

elif nAtividade == 3:
    #um pequeno programa que calcule o seu peso ideal
    Altura= float(input('Sua altura: '))
    PesoIdeal = (Altura-100) * 0.9
    print ('\nSeu peso ideal é:',PesoIdeal) 