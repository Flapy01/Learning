#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
notas.append(float(input("Digite nota 1: ")))
notas.append(float(input("Digite nota 2: ")))
notas.append(float(input("Digite nota 3: ")))
notas.append(float(input("Digite nota 4: ")))
notas_sum = sum(notas)
print("A soma das notas é: ", notas_sum)
print("E a média é: ", notas_sum / 4)