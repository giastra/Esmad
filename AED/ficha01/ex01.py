#uma central de todas as atividades do exercicios 1
print('\nUma central de todas as atividades do exercicio 1\n\n\t1-Conversor de temperatura ºC -> Fº\n\t2-Um pequeno teste de cadastro\n\t3-Calculo de peso ideal\n\t4-Calculador de IMC\n\t5-Verificar se o número é impar ou par\n\t6-Conversor de segundos em dia/hora/minuto\n\t7-Calculadora de batimento cardiaco\n\t8-Simulador de peso idal v.2\n\t9-IMC com separação de classe\n\t10-Simulador do seu peso noutro Planeta')
while True: 
    NAtividade = int(input('\nIndique qual atividade que deseja visualizar: '))
    match NAtividade:
        case 1:
            #um conversor de (t)emperatura
            TCelsius=float(input('A temperatura em Cº: '))
            TFahrenheit=(1.8*TCelsius+32)
            print('\nA temperatura em Fº {:.2f}'.format(TFahrenheit))
            break

        case 2:
            #um programa que solicite ao utilizador para indicar o seu nome próprio  (primeiro nome) 
            # e o seu apelido (sobrenome), e apresente o resultado no formato Apelido, Nome 
            Nome=input('Nome proprio: ')
            Apelido=input('\nApelido: ')
            print ('\n %s, %s'%(Apelido,Nome))
            break

        case 3:
            #um pequeno programa que calcule o seu peso ideal
            Altura= float(input('Sua altura em m ou cm: '))
            if Altura<=3:
                Altura=Altura*100
            PesoIdeal = (Altura-100) * 0.9
            print (f'\nSeu peso ideal é: {PesoIdeal}')
            break 

        case 4:
            #um simulador de índice de massa corporal (versão 1.0), pedindo 
            #ao utilizador a indicação do seu peso(em kg) e da sua altura (em metros). 
            #Calcule o respetivo índice de massa corporal (IMC)
            Peso=float(input('\nSeu peso em kg: '))
            Altura=float(input('\nSua altura em m ou cm: '))
            #caso a altura seja em cm
            if Altura >= 5:
                Altura=Altura*0.01
            Imc=Peso/pow(Altura, 2)
            print('\nO seu IMC é: {:.2f}'.format(Imc))
            break
        
        case 5:
            #calcula se o numero inteiro é par ou impar
            Numero=int(input('Escolha um numero INTEIRO: '))
            if Numero%2==0:
                print('\nO numero escolhido é par')
            else:
                print('\nO numero escolhido é impar')
            break

        case 6:
            #conversor de segundos em horas/minutos/segundos
            Segundos=float(input('Indique o tempo em SEGUNDOS: '))
            Minutos=Segundos/60
            Horas=Minutos/60
            Dias=Horas/24
            print('\nDias {:.2f}/ Horas {:.2f}/ Munutos {:.2f}/ Segundos {:.2f}'.format(Dias,Horas,Minutos,Segundos))
            break

        case 7:
            #calculadora de batimento cardiaco
            Sexo=str(input('Indique o sexo F/M: '))
            Idade=int(input('Indique a idade: '))
            match Sexo.upper:
                case 'F':bpm = 224
                case _: bpm = 220
            print(f'\nSua frequencia cardiaca maxíma é: {bpm - Idade} bpm')
            break

        case 8:
            #simulador de peso ideal com separação de sexo
            Sexo=str(input('Indique o sexo F/M: '))
            Altura=int(input('Indique a altura em m ou cm: '))
            #caso a altura seja em metros
            if Altura <=3:
                Altura=Altura*100
            match Sexo.upper: 
                case 'F': k =2
                case _: k = 4
            Peso= (Altura-100) - (Altura-150)/k
            print('\nSeu peso ideal é: {:.2f}'.format(Peso))
            break

        case 9:
            #categorizar o indivíduo, em função do índice de IMC obtido
            Peso=float(input('\nSeu peso em kg: '))
            Altura=float(input('\nSua altura em m ou cm: '))
            #caso a altura seja em cm
            if Altura >= 5:
                Altura=Altura*0.01
            Imc=Peso/pow(Altura, 2)
            print('\nO seu IMC é: {:.2f}'.format(Imc))
            if Imc <= 18.5:
                print('   Baixo do peso')
            elif Imc <= 24.9:
                print('   Peso Normal')
            elif Imc <= 29.9:
                print('   Acima do Peso')
            elif Imc <= 34.9:
                print('   Obisedade Grau I')
            elif Imc <= 39.9:
                print('   Obisedade Grau II')
            else:
                print('   Obisedade Morbida')  
            break   

        case 10:
            Peso=float(input('Indique o seu peso em kg: '))
            print('Código   Planeta      Gravidade ')   
            print('----------------------------------')
            print('   1      Mercúrio     0,37')   
            print('   2      Vénus        0,90')   
            print('   3      Marte        0,37')   
            print('   4      Júpiter      2,53')   
            print('   5      Saturno      1,06')   
            print('   6      Urano        0,91')
            Planeta=int(input('Introduza o Código do planeta escolhido: '))
            match Planeta:
                case 1: 
                    g=0.37 
                    NomePlaneta = 'Mercúrio'
                case 2:
                    g=0.90 
                    NomePlaneta = 'Vénus'
                case 3:
                    g=0.37 
                    NomePlaneta = 'Merte'
                case 4:
                    g=2.53 
                    NomePlaneta = 'Júpiter'
                case 5:
                    g=1.06 
                    NomePlaneta = 'Saturno'
                case 6:
                    g=0.91 
                    NomePlaneta = 'Urano'
            Peso=Peso*g
            print('\nSeu peso em {NomePlaneta} é de: {:.f}'.format(NomePlaneta,Peso))    
            break

        #uma forma de impedir que o utilizador escolha algo que não existe
        case _:
            print('\nAtividade não identificada, tente novamente.')
