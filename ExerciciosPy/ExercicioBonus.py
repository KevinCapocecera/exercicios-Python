num = [2, 1, 3, 62, 58, 95, 125, 47, 35, 62, 0, 8, 13, 51]
ordenar = 0
for i in range(0, len(num)):
    for j in range(0, len(num)):
        if num[i] < num[j]:
            ordenar = num[i]
            num[i] = num[j]
            num[j] = ordenar
print(num)
