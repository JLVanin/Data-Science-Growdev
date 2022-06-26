# 4) Faça um Programa que leia dois vetores com 10 elementos cada. Gere um
# terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
# elementos intercalados dos dois outros vetores.

vet_1 = []
vet_2 = []

for i in range(3):
    lista_1 = int(input(f'1° Vetor número na posição {i}: '))
    vet_1.append(lista_1)
  
for i in range(3):
    lista_2 = int(input(f'2° Vetor número na posição {i}: '))
    vet_2.append(lista_2)

print(vet_1)
print(vet_2)

def intercalar(vet_1,vet_2):
    lista = []
    for vet_1,vet_2 in zip(vet_1, vet_2):
        lista.append(vet_1)
        lista.append(vet_2)
    return lista
vetor_3 = intercalar(vet_1, vet_2)

for i in vetor_3:
    print(i ,end=" ")