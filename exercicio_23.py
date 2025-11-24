# 23 - Verifique se os valores de num1 consta nos elementosde lista1.

num1 = 100
lista1 = [10, 100, 1000, 10000, 100000]

for i in lista1:
    if i == 100:
        print(num1 in lista1)
    else:
        print(num1 not in lista1)

# outra opção:
print(num1 in lista1)
