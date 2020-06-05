from time import sleep
i = 0
print("Qual o filme que mais combina com seu sentimento atual?\nDESCUBRA AQUI!!!")
while i == 0:
    print(
        """Digite o número correspondente a opções abaixo: \n[1]FELIZ\n[2]AFIM DE CURTI A BAD\n[3]APAIXONADO\n[4]RAIVA\n[5]INTELIGENTE""")
    sleep(1)
    sent = int(input("Então, como você está?: "))
    print("Hummm....")
    sleep(2)
    if sent == 1:
        print("Minha Mãe É Uma Peça 1,2 e 3\nÉ um ótimo filme para assistir quando você está se sentindo com tudo!")

    if sent == 2:
        print(
            "Marley & Eu\nÉ uma ótima escolha para se afundar ainda mais naquela bad da quarentena.")

    if sent == 3:
        print("50 Tons De Cinza\nUm filme drámatico e picante, que vai mexer com seus sentimentos apaixonadinhos")
    if sent == 4:
        print(
            "Casamento Sangrento\nJá estava com raiva né? Então esse filme é aquela pessoa que fala: Vai ficar tudo bem.\nE você tem vontade de espancar ela. Decepcionante...")

    if sent == 5:
        print("Interestelar\nSe você está se sentindo um gênio, esse filme é para você!!")

    else:
        print("Tente novamente e digite um valor válido")
        print("Recarregando.....")
        sleep(2)
    dnv = int(input("Chame outra pessoa e tente denovo! [1]Já chamei!, [2]Já deu...?: "))
    if dnv == 2:
        break
