# 2) Escrever um programa que lê um valor N inteiro e positivo e que calcula seu
# valor fatorial. Ex: 5! = 5 * 4 * 3 * 2 * 1
num = int(input('Digite um número: '))
if num < 0:
    print('Não existe valor fatorial de números negativos.')
fatorial = 1
for num in range(num, 1, -1):
    fatorial *= num
    num -= num
print(f'O valor fatorial é {fatorial}')
