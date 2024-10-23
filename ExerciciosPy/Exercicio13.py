contagem = 0

for i in range(0, 3):
    num = int(input("digite um valor: \n"))
    if 0 < num < 100:
        contagem += 1
print("A quantidade de numeros de 0 a 100 digitada é: ", contagem)