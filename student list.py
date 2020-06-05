import time
aluno = []
def lista(escolha):
    if escolha == 1:
        aluno.append(str(input("Digite o nome do aluno: ")))
    if escolha == 2:
        aluno.remove(str(input("Digite o nome do aluno que você quer remover: ")))
    if escolha == 3:
        print(aluno)

print('{:^30}'.format('INICIANDO LISTA DE ALUNOS...'))
i = 0
while i == 0:
    print("=" * 40)
    time.sleep(2)
    print('{:^26}'.format('O QUE VOCÊ DESEJA FAZER?'))
    print("=" * 40)
    time.sleep(2)
    escolha = int(input("\n[1] Cadastrar aluno\n[2] Remover aluno\n[3] Exibir lista\n[0] Sair do programa\nDigite o número corresondente a opção desejada: "))
    print("=" * 40)
    if escolha == 0:
        print(aluno)
        break
    if escolha <= 3:
        print(f"{lista(escolha)}")
        print(aluno)




