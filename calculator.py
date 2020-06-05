print("Calculadora!!")
i = 0
while i == 0:
    n1 = float(input("Digite um número: "))
    n2 = float(input("Agora digite outro número: "))
    print("[1]SOMAR\n[2]SUBTRAIR\n[3]MULTIPLICAR\n[4]DIVIDIR\n[5]RESTO\n[6]POTENCIAÇÃO")
    op = int(input("Agora digite o número correspondente a operação desejada: "))
    if op == 1:
        print("O Resultado é:", n1 + n2)
    if op == 2:
        print("O Resultado é:", n1 - n2)
    if op == 3:
        print("O Resultado é:", n1 * n2)
    if op == 4:
        print("O Resultado é:", n1 / n2)
    if op == 5:
        print("O Resultado é:", n1 % n2)
    if op == 6:
        print("O Resultado é:", n1 ** n2)
    ag = int(input("Quer tentar denovo? [1]SIM [2]NÃO: "))
    if ag == 2:
        break
