num = [2, 1, 3, 62, 58, 95, 125, 47, 35, 62, 0, 8, 13, 51]
arrayInvertido = []

for i in range(0, len(num)):
    arrayInvertido.append(num[len(num) - 1 - i])

print(arrayInvertido)