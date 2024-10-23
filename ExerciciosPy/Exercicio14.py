contagem01 = 0
contagem02 = 0
contagem03 = 0

for i in range(0, 3):
    num = int(input("digite um valor: \n"))
    if 0 < num <= 100:
        contagem01 += 1
    elif 100 < num <= 200:
        contagem02 += 1
    elif num > 200:
        contagem03 += 1
print("A quantidade de numeros de 0 a 100 digitada foi: ", contagem01)
print("A quantidade de numeros de 100 a 200 digitada foi: ", contagem02)
print("A quantidade de numeros acima de 200 digitada foi: ", contagem03)