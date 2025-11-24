# 8 - Peça para que o usuário digite um número,
# em seguida o converta para float, exibindo em tela
# tanto o número em si quanto seu tipo de dado:

num = input("Digite um número: ")
num_float = float(num)

print(f"O número digitado foi {num_float} e ele é do tipo {type(num_float)}")
