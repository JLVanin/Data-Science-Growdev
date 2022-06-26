# 30) Ler um número inteiro (assuma até três dígitos) e imprimir a saída da
# seguinte forma:
# CENTENA = x
# DEZENA = x
# UNIDADE = x
# Exemplo: 357 tem 3 centenas, 5 dezenas e 7 unidades.

num = int(input('Informe um número: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10

print(f'O número {num} tem {cen} centenas, {dez} dezenas e {uni} unidades.')