# Ceie um programa que realiza a contagem de 1 até 100, usando apenas
# números ímpares, ao final do processo exiba em tela quantos número ímpares
# foram encontrados nesse intervalo, assim como a soma dos mesmos:

contador = []
soma = 0

for i in range(1, 101):
    if i % 2 != 0:
        contador.append(i)
        soma += i

print(f"Foram encontrados {len(contador)} números ímpares.")
print(f"A soma destes números é: {soma}")
