
import random
#uma central para os exercicios da ficha 02
print('Uma central de todas as atividades do exercicio 2\n 1-Fatorial\n 2-Soma de numeros pares\n3-Jogo do numero escondido\n4-Verifica se o numero é primo\n5-Sequência de Fibonacci\n6-Numero perfeito\n7-calculadora de binario ')
while True:
    NAtividade=int(input('\nIndique o numero da atividade que deseja visualizar: '))
    if NAtividade == 1:
        Numero=int(input('\nIndique o numero inteiro para a fatorial: '))
        Fator=1
        n=0
        while n < Numero:
            if Numero == 0:
                break
            Fator=(Numero-n)*Fator
            n+=1
        print(f'\n{Numero}! = {Fator}')    
        break
    elif NAtividade == 2:
        while True:
            NInferior=int(input('\nIndique um numero inteiro: '))
            NSuperior=int(input('\nIndique um numero inteiro maior que o anterior: '))
            n=NInferior
            Soma=0
            if NSuperior < NInferior:
                print('\nNumeros não validos introduza novamente')
                continue
            while n<=NSuperior:
                if n%2==0:
                    Soma+=n
                n+=1
            print(f'\nA soma de todos os numeros pares entre {NInferior} e {NSuperior} é {Soma}')
            break
        break
    elif NAtividade == 3:
        while True:   
            Numero = random.randint(1,50)
            print('\nBem vindo ao jogo das adivinhações, basta acertar o numero escondido entre 1 a 50, você tem 10 tentativas para acertar')
            NTentativas=1
            while NTentativas <=10:
                NInserido=int(input(f'\nIndique a sua {NTentativas}º escolha: '))
                if NInserido == Numero:
                    print(f'\nVoce conseguiu !!!, achou o numero escondido em {NTentativas} tentativas')
                    break
                elif NInserido > Numero:
                    print('O numero escondido é menor')
                elif NInserido < Numero:
                    print ('O numero escondido é maior')
                NTentativas+=1
            if NInserido != Numero:
                print (f'\nVoce perdeu :( o numero escondido era {Numero})')
            Tentar=str(input('\nVoce quer jogar novamente (s/n): '))
            if Tentar == 'n':
                break
        break
    elif NAtividade == 4:
        Numero=int(input('\nIntroduza o numero que você quer testar se é primo ou não: '))
        if Numero %2 ==0 and Numero != 2:
            print('Ele não é primo')
        elif Numero %3 ==0 and Numero != 3:
            print('Ele não é primo')
        elif Numero %5 ==0 and Numero != 5:
            print('Ele não é primo')
        elif Numero %11 ==0 and Numero != 11:
            print('Ele não é primo')
        else:
            print('ele é primo')
        break
    elif NAtividade == 5:
        Numero=int(input('Escolha quantos numeros de .... você quer ver: '))
        n=1
        print('| 0 | ',end='')
        while n <  Numero:
            Formula= (1/pow( 5,0.5))*(pow((1+pow(5,0.5))/2,n)-pow((1-pow(5,0.5))/2,n))
            print('| {:.0f} | '.format(Formula),end="")
            n+=1
        break
    elif NAtividade == 6:
        Numero=int(input('Introduza um numero positivo interiro: '))
        n=2
        e=1
        print('a soma dos divizores é : 1',end='')
        while n<Numero:
            if Numero%n ==0:
                e=e+n
                print(f' + {n}',end='')
            n+=1
        print(f' = {e}')
        if e == Numero:
            print (' Logo é perfeito')
        else:
            print(' Logo não é perfeito')     
        break
    elif NAtividade==7:
        q=int(input('um numero '))
        b=('')
        while q >= 1:
            r=abs(q%2)
            if r >0:
                d=('1')
            else:
                d=('0')
            b = (d + ' ' + b)
            print(r)
            q=q/2
            print(q)
        print(b)
        break
    elif NAtividade == 8:
        Numero=int(input('Quantidade de numeros: '))
        e = 0
        f = 1
        while Numero > 0:
            n = float(input('introduza um numero: '))
            if n > f:
                e=f
                f=n
            Numero -=1
        print('O segundo maior numer é: ',e)
        break
    else:
        print('\n - Numero não valido, tente novamente.')