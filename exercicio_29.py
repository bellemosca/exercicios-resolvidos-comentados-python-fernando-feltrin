# Crie um programa que lê um valor de início e um valor de fim,
# exibindo em tela a contagem dos números dentro desse intervalo:

inicio = int(input("Digite um número para começar: "))
fim = int(input("Digite um número para terminar: "))

for n in range(inicio, fim + 1):
    print(n)
