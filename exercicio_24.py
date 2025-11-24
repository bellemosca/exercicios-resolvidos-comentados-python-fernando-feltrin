# 24 - Crie duas variáveis com dois valores numéricos inteiros digitados
# pelo usuário, caso o valore do primeiro número for maior que o segundo,
# exiba em tela uma mensagem de acordo, caso contrário, exiba em tela uma
# mensagem dizendo que o primeiro valor digitado é menor que o segundo:

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}")
else:
    print(f"{num2} é maior que {num1}")
