# Crie um programa que pede ao usuário que o mesmo digite um número
# qualquer, em seguida retorne esse número é primo ou não, caso não, retorne
# também quantas vezes esse número é divisível:

num = int(input("Digite um número: "))
divisao = 0

for i in range(1, num + 1):
    if num % i == 0:
        divisao += 1


if divisao == 2:
    print(f"O {num} é primo.")
    print(f"{num} é divisível por 1 ou {num}.")
else:
    print(f"O {num} não é primo.")
    print(f"{num} é divisível {divisao} vezes.")
