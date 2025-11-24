# Crie um programa que realiza a Progressão Aritimética de 20 elementos,
# com primeiro termo e razão definidos pelo usuário:

a1 = int(input("Digite o primeiro termo da progressão: "))
r = int(input("Digite a razão da progressão: "))
n = 20
contador = 0
sequencia = []

while contador < n:
    sequencia.append(a1)
    a1 = a1 + r
    contador += 1

print(sequencia)
