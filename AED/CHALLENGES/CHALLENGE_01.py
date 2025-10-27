from random import randint

#criação da senha
n1=str(randint(0,9))
n2=str(randint(0,9))
n3=str(randint(0,9))
n4=str(randint(0,9))
#variaves secondarias
turnos=0
viroria=False

# mensagem inicial 
print('\t---JOGO DO COFRE---')
print(f'\n  Tente adivinhar a senha do cofre,\n a senha tem 4 numeros dentre 0 a 9,\n você tem 10 tentativas \n\n-a senha deve ser intruduzida\n tendo espaços entre os numeros ex: {n1} {n2} {n3} {n4} -')

#controlador de tentativas
while turnos<10:
    
    print(f'\nNumero de tentativas restantes {10-turnos}')
    
    Tentativa=(str(input('\nsenha : ')))
   
    # codigo para encerrar mais cedo
    if Tentativa == 'end':
            break
      
    # controladores 
    L_Tentativa=Tentativa.split(' ')        
    turnos+=1
        
    # para impedir possiveis bugs e verificaçoes erradas da senha
    if len(Tentativa) != 7 :
            print ('\n  - Formato não valido - ')
            continue

    # verifica se a sequencia está correta  
    if Tentativa == f'{n1} {n2} {n3} {n4}':
            print('\n\tcorreto')
            viroria=True
            break
        
    # verifica o 1ª numero 
    if Tentativa.find(n1) != -1:
            print(f'\n{L_Tentativa[0]} esta correto ',end='')
            
            #verifica se a posição está correta
            if L_Tentativa[0] == n1:
                print('e na possição certa')
            else:
                print('e na possição errada')

    # verifica o 2ª numero         
    if Tentativa.find(n2) != -1:
            print(f'\n{L_Tentativa[1]} esta correto ',end='')
            
            #verifica se a posição está correta
            if L_Tentativa[1] == n2:
                print('e na possição certa')
            else:
                print('e na possição errada')
        
    # verifica o 3ª numero 
    if Tentativa.find(n3) != -1:
            print(f'\n{L_Tentativa[2]} esta correto ',end='')
            
            #verifica se a posição está correta
            if L_Tentativa[2] == n3:
                print('e na possição certa')
            else:
                print('e na possição errada')

    # verifica o 4ª numero    
    if Tentativa.find(n4) != -1:
            print(f'\n{L_Tentativa[3]} esta correto ',end='')
            
            #verifica se a posição está correta
            if L_Tentativa[3] == n4:
                print('e na possição certa')
            else:
                print('e na possição errada')
        
        
#condição de derrota
if viroria == False:
    print('\n\tTentativas esgotadas, tente novamente mais tarde')
    

