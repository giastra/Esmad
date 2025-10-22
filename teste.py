from sys import exit
status='\nO aluno foi classificado como'
print('\nBaco de dados das classificaçoes dos alunos\n\ttodas as informaçoes serão salvas em : alunostatus.txt')
while True:
    nome = str(input("\n  : Digite o nome do aluno \n\t(para encerrar o programa introduza 'sair') : ")).strip().title()
    nomoNome= nome.split(' ')
    
    if nome == 'Sair':
        print('\nPrograma encerrado.')
        exit()

    try:
        nota = float(input(f"\n\tDigite a nota do aluno {nomoNome[0]} : "))
    
    except ValueError:
        print("\nO valor da nota deve ser um número")
        print("-\n\t- Reinicie o programa -")
        break
    
    if nota >= 7:
        print(f'{status} -Aprovado-')
        status_aluno = "APROVADO"
    elif nota >= 6:
        print(f'{status} -Recuperação-')
        status_aluno = "RECUPERAÇÃO"
    else:
        print(f'{status} -Reprovado-')
        status_aluno = "REPROVADO"

    with open('alunostatus.txt', 'a', encoding='utf-8') as file:
        file.writelines(f"Aluno: {nome} | Sitatus: {status_aluno} | Nota: {nota}\n")
    print('\n\tInformações anotadas, pronto para o proximo aluno')