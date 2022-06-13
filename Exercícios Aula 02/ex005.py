#5) Escreva um programa que receba como entrada a quantidade de torcedores
#do time X, do time Y e do time Z, calcula e exibe qual a porcentagem de torcedores de cada time.

time_x = int(input('Quantidade de torcedores do time X: '))
time_y = int(input('Quantidade de torcedores do time Y: '))
time_z = int(input('Quantidade de torcedores do time Z: '))
total = time_x + time_y + time_z
print('Time X tem {} Torcedores ({:.2f}%) '.format(time_x, (time_x/total*100)))
print('Time Y tem {} Torcedores ({:.2f}%) '.format(time_y, (time_y/total*100)))
print('Time Z tem {} Torcedores ({:.2f}%) '.format(time_z, (time_z/total*100)))