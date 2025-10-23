from random import randint
n1=str(randint(0,9))
n2=str(randint(0,9))
n3=str(randint(0,9))
n4=str(randint(0,9))
turnos=0
viroria=False
print(f'{n1} {n2} {n3} {n4}')
while turnos<10:
    Tentativa=str(input('senha : '))
    L_Tentativa=Tentativa.split(' ')
    turnos+=1
    print(f'Numero de tentativas restantes {10-turnos}')
    if Tentativa == f'{n1} {n2} {n3} {n4}':
        print('correto')
        viroria=True
        break
    if L_Tentativa[0] == n1:
        print('A primeira esta certa')
    if L_Tentativa[1] == n2:
        print('A segunda esta certa')
    if L_Tentativa[2] == n3:
        print('A terceira esta certa')
    if L_Tentativa[3] == n4:
        print('A quarta esta certa')
if viroria == False:
    print('Tentativas esgotadas, tente novamente mais tarde')
    

