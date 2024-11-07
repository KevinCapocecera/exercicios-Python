num = [2, 1, 3, 62, 58, 95, 125, 47, 35, 62, 0, 8, 13, 51]

menor = num[0]
maior = num[0]

for i in range(0, len(num)):
    if num[i] < menor:
        menor = num[i]
    elif num[i] > maior:
        maior = num[i]

print("O menor valor digitado foi: ", menor)
print("O maior valor digitado foi: ", maior)